import argparse
import datetime
import json
from object.account import *
import sys


def recruit_troops(vm_name):
    # Recruit Troops
    # -- Recruit camp
    vm.handle_if_game_not_open(vm_index, vm_name)
    game.handle_recruit_troop(vm_index, building_type='camp', number=1)
    game.handle_recruit_troop(vm_index, building_type='camp', number=2)
    # -- Recruit Factory
    vm.handle_if_game_not_open(vm_index, vm_name)
    game.handle_recruit_troop(vm_index, building_type='factory', number=1)
    game.handle_recruit_troop(vm_index, building_type='factory', number=2)


def gather_resources(level, gather_type, resource_level, vm_name):
    vm.handle_if_game_not_open(vm_index, vm_name)

    if gather_type != '' and int(level) < 15:
        game.handle_gather_resources(vm_index, 'oil', resource_level)
    elif gather_type == 'farm':
        game.handle_gather_resources(vm_index, 'farm', resource_level)
    elif gather_type == 'steel':
        game.handle_gather_resources(vm_index, 'steel', resource_level)
    elif gather_type == 'mineral':
        game.handle_gather_resources(vm_index, 'mineral', resource_level)
    else:
        game.handle_gather_resources(vm_index, 'oil', resource_level)


def check_limit_instances():
        while True:
            instances_running_count = vm.count_tasks('MEmu.exe')
            print("current instances: " + str(instances_running_count))
            if instances_running_count >= 1:
                time.sleep(60)
            else:
                break
        return


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--gather-resources-type', '-g', help='Resources type to gather', choices=['oil', 'farm', 'steel', 'mineral'], default='oil')
    parser.add_argument('--config-file', '-f', help='Config file for accounts [.\\config.json]', required=True)
    parser.add_argument('--command', '-c', help='Single command automation', choices=['withdraw', 'explore', 'instant'])
    parser.add_argument('--wait', '-w', help='Wait until runtime')
    parser.add_argument('--restart', '-r', help='Restart Mode, set repeat to only 1', action='store_true')
    args = parser.parse_args()

    gather_resources_type = args.gather_resources_type
    config_file = open(args.config_file)
    config = json.load(config_file)
    config_file.close()
    vm_index = int(config["vm_index"])
    vm_title = config["vm_name"]
    # Start Debugging Area
    # sys.exit(-1)
    # End Debugging Area
    sleep_time = config["sleep_interval"]
    accounts = Accounts(vm_index, [])
    linked_accounts = dict()
    for i, email_account in enumerate(config['accounts']):
        linked_accounts[i] = EmailAccount([])
        for account in email_account:
            linked_accounts[i].add(Account(account['name'], account['level'], account['target_upgrade'], account['target_research']))
        accounts.add(linked_accounts[i])
    interval_hour = config["interval_hour"]
    current_hour = datetime.datetime.now().hour
    last_hour = current_hour - interval_hour
    if hasattr(args, 'wait') and args.wait is not None:
        time.sleep(int(args.wait))
    if hasattr(args, 'command') and args.command is not None:
        if args.command == 'withdraw':
            game.withdraw_fleet(vm_index, accounts, config)
        elif args.command == 'explore':
            game.explore_ruin(vm_index, accounts, config)
        elif args.command == 'instant':
            game.instant_recall(vm_index, accounts, config)
        sys.exit(-1)

    already_run_once = False
    while True:
        if not already_run_once or not args.restart:
            vm.clear_caches(vm_index)
            pass
        check_limit_instances()
        vm.handle_if_game_not_open(vm_index, config['vm_name'])
        for i, email in enumerate(config['accounts']):
            for j, account in enumerate(email):
                account = Account(account['name'], account['level'], account['target_upgrade'], account['target_research'])
                accounts.switch_account(i, j)

                print(account.name)
                account_level = int(account.level)
                time.sleep(5)
                if account_level >= 19:
                    repeat = 4
                elif account_level >= 12:
                    repeat = 3
                else:
                    repeat = 2
                #  If account level is 15 or higher, gather steel otherwise gather oil or whatever assigned
                if already_run_once or args.restart:
                    # repeat = 3
                    pass
                else:
                    game.collect_daily_reward(vm_index)
                    game.collect_territory_reward(vm_index)

                if int(config["recruit_frequency"]) == 2:
                    recruit_troops(config['vm_name'])

                for r in range(0, repeat):
                    gather_resources(account_level, gather_resources_type, config['resource_level'], config['vm_name'])
                #  Collect resources and activate harvest every interval hour
                # print(f"current hour: {current_hour} | last hour: {last_hour}")
                if last_hour + interval_hour <= current_hour or current_hour + interval_hour < last_hour:
                    if not args.restart:
                        if int(config['recruit_frequency']) == 1:
                            recruit_troops(config['vm_name'])
                        # Collect Resources & activate harvest
                        game.handle_collect_resources(vm_index, account_level)
                        game.handle_activate_harvest(vm_index)
                        # Help alliances and upgrade targeted building
                        game.help_alliances(vm_index)
                        game.handle_upgrade_targeted_building(vm_index, account)
            if i < len(config['accounts']) - 1:
                vm.restart_app(vm_index, config['vm_name'])
        if last_hour + interval_hour <= current_hour or current_hour + interval_hour < last_hour:
            last_hour = current_hour
        vm.stop_vm(vm_index, config['vm_name'])
        current_hour = datetime.datetime.now().hour
        already_run_once = True
        args.restart = False
        print(datetime.datetime.now())
        time.sleep(sleep_time)

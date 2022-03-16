import argparse
import datetime
import json
from object.account import *
import sys


def recruit_troops(pid):
    # Recruit Troops
    # -- Recruit camp
    pid = vm.handle_if_game_not_open(vm_index, pid)
    game.handle_recruit_troop(vm_index, building_type='camp', number=1)
    game.handle_recruit_troop(vm_index, building_type='camp', number=2)
    # -- Recruit Factory
    pid = vm.handle_if_game_not_open(vm_index, pid)
    game.handle_recruit_troop(vm_index, building_type='factory', number=1)
    game.handle_recruit_troop(vm_index, building_type='factory', number=2)
    return pid


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--gather-resources-type', '-g', help='Resources type to gather', choices=['oil', 'farm', 'steel', 'mineral'], default='oil')
    parser.add_argument('--vm-index', '-i', help='Index value of Memu Emulator', default=0)
    parser.add_argument('--config-file', '-f', help='Config file for accounts [.\\config.json]', required=True)
    parser.add_argument('--command', '-c', help='Single command automation', choices=['withdraw', 'explore'])
    args = parser.parse_args()

    gather_resources_type = args.gather_resources_type
    vm_index = args.vm_index
    config_file = open(args.config_file)
    config = json.load(config_file)
    config_file.close()

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
    pid = 0
    if hasattr(args, 'command') and args.command is not None:
        if args.command == 'withdraw':
            game.withdraw_fleet(vm_index, accounts, config)
        elif args.command == 'explore':
            game.explore_ruin(vm_index, accounts, config)
        sys.exit(-1)
    # Start Debugging Area
    # vm.start_game(vm_index)
    # vm.handle_if_game_not_open(vm_index)
    # End Debugging Area
    already_run_once = False
    while True:
        pid = vm.handle_if_game_not_open(vm_index, pid)
        print(pid)
        for i, email in enumerate(config['accounts']):
            for j, account in enumerate(email):
                account = Account(account['name'], account['level'], account['target_upgrade'], account['target_research'])
                accounts.switch_account(i, j)

                print(account.name)
                account_level = int(account.level)
                time.sleep(5)

                #  If account level is 15 or higher, gather steel otherwise gather oil or whatever assigned
                if already_run_once:
                    repeat = 1
                else:
                    repeat = 2
                for r in range(0, repeat):
                    if account_level >= 15:
                        pid = vm.handle_if_game_not_open(vm_index, pid)
                        game.handle_gather_resources(vm_index, 'steel')
                    else:
                        if gather_resources_type == 'farm':
                            pid = vm.handle_if_game_not_open(vm_index, pid)
                            game.handle_gather_resources(vm_index, 'farm')
                        else:
                            pid = vm.handle_if_game_not_open(vm_index, pid)
                            game.handle_gather_resources(vm_index, 'oil')
                if config["increase_recruit"]:
                    pid = recruit_troops(pid)

                #  Collect resources and activate harvest every one hour
                print(f"current hour: {current_hour} | last hour: {last_hour}")
                if last_hour + interval_hour <= current_hour:
                    if not config["increase_recruit"]:
                        pid = recruit_troops(pid)
                    # Collect Resources & activate harvest
                    pid = vm.handle_if_game_not_open(vm_index, pid)
                    game.handle_collect_resources(vm_index)
                    game.handle_activate_harvest(vm_index)
                    # Help alliances and upgrade targeted building
                    pid = vm.handle_if_game_not_open(vm_index, pid)
                    game.help_alliances(vm_index)
                    game.handle_upgrade_targeted_building(vm_index, account)
        if last_hour + interval_hour <= current_hour:
            last_hour = current_hour
        vm.stop_vm(vm_index, pid)
        current_hour = datetime.datetime.now().hour
        already_run_once = True
        print(datetime.datetime.now())
        time.sleep(sleep_time)

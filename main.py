import argparse
import datetime
import json
from object.account import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--gather-resources-type', help='resources type to gather [oil|steel|farm], default is oil')
    parser.add_argument('--vm-index', help='Index value of Memu Emulator e.g 0|1|2|3')
    parser.add_argument('--config-file', help='Config file for accounts [.\\config.json]')
    parser.add_argument('--command', help='Single command [recall|explore|sendalltroops]')
    args = parser.parse_args()

    gather_resources_type = 'oil'
    vm_index = 0
    if hasattr(args, 'gather_resources_type') and args.gather_resources_type is not None:
        gather_resources_type = args.gather_resources_type
    if hasattr(args, 'vm_index') and args.vm_index is not None:
        vm_index = args.vm_index
    if hasattr(args, 'command') and args.command is not None:
        if args.command == 'recall':
            print("recall")
        elif args.command == 'explore':
            print('explore')
        elif args.command == 'sendalltroops':
            print('send all troops')
        else:
            print("Error: Invalid command!")
        exit(-1)
    elif hasattr(args, 'config_file') and args.config_file is not None:
        config_file = open(args.config_file)
        config = json.load(config_file)
        config_file.close()
    else:
        print('Config file is missing!')
        exit(-1)

    # Start Debugging Area
    # vm.start_game(vm_index)
    vm.handle_if_game_not_open(vm_index)
    exit(-1)
    # End Debugging Area
    accounts = Accounts(vm_index, [])
    linked_accounts = dict()
    for i, email_account in enumerate(config['accounts']):
        linked_accounts[i] = EmailAccount([])
        for account in email_account:
            linked_accounts[i].add(Account(account['name'], account['level'], account['target_upgrade'], account['target_research']))
        accounts.add(linked_accounts[i])
    interval_hour = 2
    current_hour = datetime.datetime.now().hour
    last_hour = current_hour - interval_hour
    while True:
        vm.handle_restart_if_game_not_open(vm_index)
        for i, email in enumerate(config['accounts']):
            for j, account in enumerate(email):
                account = Account(account['name'], account['level'], account['target_upgrade'], account['target_research'])
                accounts.switch_account(i, j)

                print(account.name)
                account_level = int(account.level)
                time.sleep(5)

                #  If account level is 15 or higher, gather steel otherwise gather oil or whatever assigned
                if account_level >= 15:
                    game.handle_gather_resources(vm_index, 'steel')
                else:
                    if gather_resources_type == 'farm':
                        game.handle_gather_resources(vm_index, 'farm')
                    else:
                        game.handle_gather_resources(vm_index, 'oil')
                #  Collect resources and activate harvest every one hour
                print(f"current hour: {current_hour} | last hour: {last_hour}")
                if last_hour + interval_hour <= current_hour:
                    game.handle_recruit_troop(vm_index, building_type='camp', number=1)
                    game.handle_recruit_troop(vm_index, building_type='camp', number=2)
                    game.handle_recruit_troop(vm_index, building_type='factory', number=1)
                    game.handle_recruit_troop(vm_index, building_type='factory', number=2)
                    # Collect Resources
                    game.handle_collect_resources(vm_index)
                    game.handle_activate_harvest(vm_index)
                    game.help_alliances(vm_index)
                    game.handle_upgrade_targeted_building(vm_index, account)
        if last_hour + interval_hour <= current_hour:
            last_hour = current_hour
        current_hour = datetime.datetime.now().hour
        vm.stop_vm("", vm_index)
        time.sleep(900)
        vm.start_vm("", vm_index)
        time.sleep(10)
        vm.start_game(vm_index)
        time.sleep(10)

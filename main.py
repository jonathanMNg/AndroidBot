import datetime
import vm
import time
import game
from object.coordinate import Coordinate
from locations import functions_location
import argparse
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--gather-resources-type', help='resources type to gather [oil|steel|farm], default is oil')
    parser.add_argument('--vm-index', help='Index value of Memu Emulator e.g 0|1|2|3')
    args = parser.parse_args()

    gather_resources_type = 'oil'
    vm_index = 0
    if hasattr(args, 'gather_resources_type'):
        gather_resources_type = args.gather_resources_type
    if hasattr(args, 'vm_index'):
        vm_index = args.vm_index

    total_accounts = len(getattr(functions_location.tab_bar.my_info.account.functions.switch_account.accounts, f"vm_index_{vm_index}"))
    #  Start Debugging Area

    # account = functions_location.tab_bar.my_info.account.functions.switch_account.accounts.vm_index_2.account_1
    # game.handle_collect_resources(vm_index)
    # game.handle_upgrade_targeted_building(vm_index, account)

    # End Debugging Area
    current_account = 0
    current_hour = datetime.datetime.now().hour
    last_hour = current_hour - 1
    while True:
        if current_account < total_accounts:
            current_account = current_account + 1
        else:
            if last_hour < current_hour:
                last_hour = current_hour
            current_hour = datetime.datetime.now().hour
            vm.stop_vm("", vm_index)
            time.sleep(600)
            vm.start_vm("", vm_index)
            time.sleep(10)
            vm.start_game(vm_index)
            time.sleep(10)
            current_account = 1

        account = game.handle_switch_account(vm_index, current_account)
        print(current_account)
        account_level = account.level
        time.sleep(5)

        game.handle_recruit_troop(vm_index, building_type='camp', number=1)
        game.handle_recruit_troop(vm_index, building_type='camp', number=2)
        game.handle_recruit_troop(vm_index, building_type='factory', number=1)
        game.handle_recruit_troop(vm_index, building_type='factory', number=2)

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
        if last_hour < current_hour:
            game.handle_collect_resources(vm_index)
            game.handle_activate_harvest(vm_index)
            game.help_alliances(vm_index)
            game.handle_upgrade_targeted_building(vm_index, account)

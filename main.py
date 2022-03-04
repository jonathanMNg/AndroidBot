import time
import vm
import game
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

    total_accounts = len(functions_location.ui.my_info.account.functions.switch_account.accounts)
    game.handle_gather_resources(vm_index, gather_resources_type)

    current_account = 0
    # while True:
    #     if current_account < total_accounts:
    #         current_account = current_account + 1
    #     else:
    #         vm.stop_vm("", vm_index)
    #         time.sleep(300)
    #         vm.start_vm("", vm_index)
    #         time.sleep(10)
    #         vm.start_game(vm_index)
    #         time.sleep(10)
    #         current_account = 1
    #
    #     vm.handle_restart_if_game_not_open(vm_index)
    #     account = game.handle_switch_account(vm_index, current_account)
    #     print(current_account)
    #     account_level = account.level
    #     time.sleep(5)
    #
    #     game.handle_recruit_camp1(vm_index)
    #
    #     game.handle_recruit_camp2(vm_index)
    #
    #     game.handle_recruit_factory1(vm_index)
    #
    #     game.handle_recruit_factory2(vm_index)
    #
    #     #  If account level is 15 or higher, gather steel otherwise gather oil or whatever assigned
    #     if account_level >= 15:
    #         game.handle_gather_resources(vm_index, 'steel')
    #     else:
    #         if gather_resources_type == 'farm':
    #             game.handle_gather_resources(vm_index, 'farm')
    #         else:
    #             game.handle_gather_resources(vm_index, 'oil')


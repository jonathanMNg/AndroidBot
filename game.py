import time
from object.coordinate import Coordinate
from locations import city_map_location, ui_location, functions_location
from helper import *
import vm


def switch_city_and_map(vm_index):
    vm.handle_touch(vm_index, 40, 615)
    time.sleep(2)


def close_all_windows(vm_index):
    vm.handle_return(vm_index)
    vm.handle_return(vm_index)
    vm.handle_return(vm_index)
    vm.handle_tap(vm_index, ui_location.battle_power_score)
    vm.handle_tap(vm_index, ui_location.battle_power_score)
    vm.handle_tap(vm_index, ui_location.battle_power_score)
    vm.handle_return(vm_index)


def go_to_city_view(vm_index):
    close_all_windows(vm_index)
    time.sleep(2)
    switch_city_and_map(vm_index)
    vm.handle_return(vm_index)
    time.sleep(2)


def handle_set_gather_resource_level(vm_index, level):
    vm.handle_touch(vm_index, 155, 575)
    vm.handle_long_tap(vm_index, Coordinate(17, 614))
    vm.handle_input(vm_index, level)
    vm.handle_enter(vm_index)


def handle_gather_resources(vm_index, resource_type):
    vm.handle_restart_if_game_not_open(vm_index)
    close_all_windows(vm_index)
    switch_city_and_map(vm_index)

    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.radar)
    if resource_type == 'farm':
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.farm)
    elif resource_type == 'steel':
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.steel)
    else:
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.oil)
    handle_set_gather_resource_level(vm_index, 4)
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.go)
    # Tap one gather to close the search view, second tap is to click on gather
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.gather)
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.gather)
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.set_out)


def handle_ui_helper_expand(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.ui_helper_expand)


def handle_recruit_troop(vm_index, building_type, number=1):
    vm.handle_restart_if_game_not_open(vm_index)
    recruit_option = 1
    ui_helper_location = None
    if building_type.lower() == 'camp':
        #  Recruit sniper only
        recruit_option = 2
        if number == 1:
            ui_helper_location = city_map_location.troop_buildings.buildings.camp_1.ui_helper
        else:
            ui_helper_location = city_map_location.troop_buildings.buildings.camp_2.ui_helper
    elif building_type.lower() == 'factory':
        #  Recruit shredder only
        recruit_option = 1
        if number == 1:
            ui_helper_location = city_map_location.troop_buildings.buildings.factory_1.ui_helper
        else:
            ui_helper_location = city_map_location.troop_buildings.buildings.factory_2.ui_helper

    # Collect troops
    # handle_ui_helper_expand(vm_index)
    # vm.handle_tap(vm_index, ui_helper_location)

    # Recruit troops
    handle_ui_helper_expand(vm_index)
    vm.handle_tap(vm_index, ui_helper_location)
    vm.handle_tap(vm_index, functions_location.buildings.troop_buildings.recruit.select_recruit)


def handle_switch_account(vm_index, account_no):
    vm.handle_restart_if_game_not_open(vm_index)
    account = None
    accounts_based_on_vm_index = getattr(functions_location.tab_bar.my_info.account.functions.switch_account.accounts, f"vm_index_{vm_index}")
    total_accounts = len(accounts_based_on_vm_index)
    if account_no in range(1, total_accounts + 1):
        account = getattr(accounts_based_on_vm_index, f"account_{account_no}")
    else:
        Exception("Invalid account: " + str(account_no))

    choose_email = account.choose_email
    choose_account = account.choose_account
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.my_info)
    vm.handle_tap(vm_index, functions_location.tab_bar.my_info.account.coordinate)
    vm.handle_tap(vm_index, functions_location.tab_bar.my_info.account.functions.switch_account.coordinate)
    vm.handle_tap(vm_index, functions_location.tab_bar.my_info.account.functions.switch_account.game_login)
    time.sleep(5)
    vm.handle_tap(vm_index, choose_email)
    time.sleep(5)
    vm.handle_tap(vm_index, choose_account)
    vm.handle_tap(vm_index, functions_location.tab_bar.my_info.account.functions.switch_account.confirm_choose_account)
    time.sleep(5)
    return account


def handle_collect_resources(vm_index):
    vm.handle_restart_if_game_not_open(vm_index)
    go_to_city_view(vm_index)
    resource_building_location = city_map_location.resource_buildings
    handle_tap_path(vm_index, resource_building_location.tap_path_from_default_view)
    vm.handle_tap(vm_index, resource_building_location.buildings.steel.coordinate)
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, resource_building_location.buildings.farm.coordinate)
    vm.handle_tap(vm_index, resource_building_location.buildings.oil.coordinate)


def handle_activate_harvest(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.activate_commander_skills.coordinate)
    vm.handle_tap(vm_index, ui_location.activate_commander_skills.functions.harvest)
    vm.handle_tap(vm_index, ui_location.activate_commander_skills.functions.use)


def handle_tap_path(vm_index, tap_path):
    for coordinate in tap_path:
        vm.handle_tap(vm_index, coordinate)


def handle_upgrade_targeted_building(vm_index, account):
    vm.handle_restart_if_game_not_open(vm_index)
    if account.upgrade_building is not None and account.upgrade_building != '':
        go_to_city_view(vm_index)
        building_type = get_building_information(account.upgrade_building.split('.')[0])
        target_building = get_building_information(account.upgrade_building)
        handle_tap_path(vm_index, building_type.tap_path_from_default_view)
        vm.handle_tap(vm_index, target_building.coordinate)
        vm.handle_tap(vm_index, target_building.functions.upgrade.coordinate)
        vm.handle_tap(vm_index, functions_location.buildings.functions.upgrade)


def help_alliances(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.alliance.coordinate)
    vm.handle_tap(vm_index, ui_location.alliance.functions.alliance_help)
    vm.handle_tap(vm_index, ui_location.alliance.functions.help_all)

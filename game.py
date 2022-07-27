import time
from object.coordinate import Coordinate
from locations import ui_location, functions_location
from helper import *
from object.account import *
import vm
from object.building import Building


def switch_city_and_map(vm_index):
    vm.handle_tap(vm_index, Coordinate(40, 615))
    time.sleep(2)


def close_all_windows(vm_index):
    vm.handle_return(vm_index)
    vm.handle_return(vm_index)
    vm.handle_return(vm_index)
    vm.handle_return(vm_index)
    vm.handle_tap(vm_index, ui_location.battle_power_score)
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
    vm.handle_tap(vm_index, Coordinate(155, 575))
    vm.handle_long_tap(vm_index, Coordinate(17, 614))
    vm.handle_input(vm_index, level)
    vm.handle_enter(vm_index)


def handle_gather_resources(vm_index, resource_type, resource_level):
    close_all_windows(vm_index)
    switch_city_and_map(vm_index)

    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.radar)
    if resource_type == 'farm':
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.farm)
    elif resource_type == 'steel':
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.steel)
    elif resource_type == 'mineral':
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.mineral)
    else:
        vm.handle_tap(vm_index, functions_location.map_view.gather.select_resource_type.oil)
    if int(resource_level) != 0:
        handle_set_gather_resource_level(vm_index, int(resource_level))
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.go)
    # Tap one gather to close the search view, second tap is to click on gather
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.gather)
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.gather)
    vm.handle_tap(vm_index, functions_location.map_view.gather.functions.set_out)


def handle_ui_helper_expand(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.ui_helper_expand)


def handle_recruit_troop(vm_index, building_type, number=1):
    # recruit_option = 1
    ui_helper_location = None
    if building_type.lower() == 'camp':
        #  Recruit sniper only
        # recruit_option = 2
        if number == 1:
            ui_helper_location = city_map_location.troop_buildings.buildings.camp_1.ui_helper
        else:
            ui_helper_location = city_map_location.troop_buildings.buildings.camp_2.ui_helper
    elif building_type.lower() == 'factory':
        #  Recruit shredder only
        # recruit_option = 1
        if number == 1:
            ui_helper_location = city_map_location.troop_buildings.buildings.factory_1.ui_helper
        else:
            ui_helper_location = city_map_location.troop_buildings.buildings.factory_2.ui_helper

    # # Collect troops
    # handle_ui_helper_expand(vm_index)
    # vm.handle_tap(vm_index, ui_helper_location)
    #
    # # Recruit troops
    # handle_ui_helper_expand(vm_index)
    # vm.handle_tap(vm_index, ui_helper_location)
    # vm.handle_tap(vm_index, functions_location.buildings.troop_buildings.recruit.select_recruit)

    # Collect and recruit troops
    handle_ui_helper_expand(vm_index)
    vm.handle_tap(vm_index, ui_helper_location)
    vm.handle_tap(vm_index, ui_helper_location)
    vm.handle_tap(vm_index, ui_helper_location)
    vm.handle_tap(vm_index, functions_location.buildings.troop_buildings.recruit.select_recruit)


def handle_switch_account(vm_index, account_no):
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


def handle_collect_resources(vm_index, account_level=10):
    go_to_city_view(vm_index)
    resource_building_location = city_map_location.resource_buildings
    handle_tap_path(vm_index, resource_building_location.tap_path_from_default_view)
    if account_level >= 15:
        vm.handle_tap(vm_index, resource_building_location.buildings.steel.coordinate)

    if account_level >= 20:
        vm.handle_tap(vm_index, resource_building_location.buildings.mineral.coordinate)
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
    if account.target_upgrade is not None and account.target_upgrade != '':
        go_to_city_view(vm_index)
        building_name = account.target_upgrade
        target_building = Building(building_name, vm_index)
        target_building.upgrade()


def help_alliances(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.alliance.coordinate)
    vm.handle_tap(vm_index, ui_location.alliance.functions.alliance_help)
    vm.handle_tap(vm_index, ui_location.alliance.functions.help_all)


def withdraw_fleet(vm_index, accounts, config, index=0):
    for i, email in enumerate(config['accounts']):
        if i < index:
            continue
        for j, account in enumerate(email):
            if vm.handle_if_game_not_open(vm_index, config["vm_name"]):
                withdraw_fleet(vm_index, accounts, config, i)
                return
            close_all_windows(vm_index)
            accounts.switch_account(i, j)
            close_all_windows(vm_index)
            switch_city_and_map(vm_index)
            time.sleep(5)
            vm.handle_tap(vm_index, Coordinate(142, 122))
            vm.handle_tap(vm_index, Coordinate(200, 353))

            vm.handle_tap(vm_index, Coordinate(142, 155))
            vm.handle_tap(vm_index, Coordinate(200, 353))

            vm.handle_tap(vm_index, Coordinate(25, 191))
            vm.handle_tap(vm_index, Coordinate(200, 353))

            vm.handle_tap(vm_index, Coordinate(142, 186))
            vm.handle_tap(vm_index, Coordinate(200, 353))

            vm.handle_tap(vm_index, Coordinate(142, 218))
            vm.handle_tap(vm_index, Coordinate(200, 353))


def explore_ruin(vm_index, accounts, config, index=0):
    for i, email in enumerate(config['accounts']):
        if i < index:
            continue
        for j, account in enumerate(email):
            if vm.handle_if_game_not_open(vm_index, config["vm_name"]):
                explore_ruin(vm_index, accounts, config, i)
                return

            close_all_windows(vm_index)
            accounts.switch_account(i, j)
            close_all_windows(vm_index)
            # Select Prosperity
            vm.handle_tap(vm_index, Coordinate(155, 10))
            # Select proceed to ruins
            vm.handle_tap(vm_index, Coordinate(200, 333))
            time.sleep(5)
            # Select Explore
            vm.handle_tap(vm_index, Coordinate(198, 181))
            time.sleep(2)
            # Select Refugee Rescue
            vm.handle_tap(vm_index, Coordinate(110, 173))
            time.sleep(2)
            # Select level
            ruins_level_coordinate = Coordinate(config["ruins_level_coordinate"]["x"], config["ruins_level_coordinate"]["y"])
            vm.handle_tap(vm_index, ruins_level_coordinate)

            # Select set out
            vm.handle_tap(vm_index, Coordinate(337, 621))


def instant_recall(vm_index, accounts, config, index=0):
    for i, email in enumerate(config['accounts']):
        if i < index:
            continue
        for j, account in enumerate(email):
            if vm.handle_if_game_not_open(vm_index, config["vm_name"]):
                instant_recall(vm_index, accounts, config, i)
                return
            close_all_windows(vm_index)
            accounts.switch_account(i, j)

            vm.handle_tap(vm_index, ui_location.activate_commander_skills.coordinate)
            vm.handle_tap(vm_index, ui_location.activate_commander_skills.functions.recall)
            vm.handle_tap(vm_index, ui_location.activate_commander_skills.functions.use)


def collect_territory_reward(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.mail)
    # Tap on the 3 dots ***
    vm.handle_tap(vm_index, Coordinate(375, 20))
    # Tap on select all mails
    vm.handle_tap(vm_index, Coordinate(119, 630))
    # Tap open all
    vm.handle_tap(vm_index, Coordinate(193, 627))


def collect_daily_reward(vm_index):
    vm.handle_tap(vm_index, Coordinate(200, 516))

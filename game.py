import time
import keyboard
from object.coordinate import Coordinate
from locations import city_map_location, ui_location, functions_location

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


def handle_setout(vm_index):
    vm.handle_touch(vm_index, 330, 620)


def handle_select_radar(vm_index):
    vm.handle_touch(vm_index, 375, 515)


def handle_select_farm(vm_index):
    vm.handle_touch(vm_index, 45, 530)


def handle_select_oil_field(vm_index):
    vm.handle_touch(vm_index, 115, 530)


def handle_select_steel_mill(vm_index):
    vm.handle_touch(vm_index, 160, 520)


def handle_select_mineral_mine(vm_index):
    vm.handle_touch(vm_index, 225, 520)


def handle_select_monster(vm_index):
    vm.handle_touch(vm_index, 345, 520)


def handle_set_gather_resource_level(vm_index, level):
    vm.handle_touch(vm_index, 155, 575)
    vm.handle_long_tap(vm_index, Coordinate(17, 614))
    vm.handle_input(vm_index, level)
    vm.handle_enter(vm_index)


def handle_select_add_button(vm_index):
    vm.handle_touch(vm_index, 275, 600)


def handle_select_go(vm_index):
    vm.handle_touch(vm_index, 351, 600)


def handle_select_resource_target(vm_index):
    vm.handle_touch(vm_index, 269, 292)


def handle_select_gather_icon(vm_index):
    vm.handle_touch(vm_index, 275, 295)


def handle_select_zombie_building(vm_index):
    vm.handle_touch(vm_index, 155, 510)


def handle_select_treatment_room(vm_index):
    vm.handle_touch(vm_index, 160, 360)


def handle_select_heal_lucy(vm_index):
    vm.handle_touch(vm_index, 100, 600)


def handle_select_heal_button(vm_index):
    vm.handle_touch(vm_index, 50, 150)


def handle_select_routine_heal(vm_index):
    vm.handle_touch(vm_index, 90, 615)


def handle_heal_zombie(vm_index):
    go_to_city_view(vm_index)
    handle_select_zombie_building(vm_index)
    handle_select_treatment_room(vm_index)
    handle_select_heal_lucy(vm_index)
    handle_select_heal_button(vm_index)
    handle_select_routine_heal(vm_index)


def handle_gather_elite_resources(vm_index):
    print()


def handle_gather_resources(vm_index, resource_type):
    vm.handle_restart_if_game_not_open(vm_index)
    close_all_windows(vm_index)
    switch_city_and_map(vm_index)

    handle_select_radar(vm_index)
    if resource_type == 'farm':
        handle_select_farm(vm_index)
    elif resource_type == 'steel':
        handle_select_steel_mill(vm_index)
    else:
        handle_select_oil_field(vm_index)
    handle_set_gather_resource_level(vm_index, 4)
    handle_select_go(vm_index)
    handle_select_resource_target(vm_index)
    handle_select_gather_icon(vm_index)
    handle_setout(vm_index)


def handle_ui_helper_expand(vm_index):
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.ui_helper_expand)


def handle_touch_building(vm_index, coordinate):
    vm.handle_tap(vm_index, coordinate)


def handle_collect_resources(vm_index, coordinate):
    go_to_city_view(vm_index)
    vm.handle_swipe_to_location(vm_index, city_map_location.resource_buildings.direction_from_default_view.horizontal,
                                city_map_location.resource_buildings.direction_from_default_view.vertical)
    handle_touch_building(vm_index, coordinate)


def handle_help_alliances(vm_index):
    go_to_city_view(vm_index)
    vm.handle_swipe_to_location(vm_index, city_map_location.troop_buildings.direction_from_default_view.horizontal,
                                city_map_location.troop_buildings.direction_from_default_view.vertical)

    handle_touch_building(vm_index, city_map_location.troop_buildings.buildings.embassy.coordinate)


def handle_recruit_troop(vm_index, building_type, number=1):
    vm.handle_restart_if_game_not_open(vm_index)
    recruit_option = 1
    building_location = None
    ui_helper_location = None
    if building_type.lower() == 'camp':
        #  Recruit sniper only
        recruit_option = 2
        if number == 1:
            building_location = city_map_location.troop_buildings.buildings.camp_1
            ui_helper_location = city_map_location.troop_buildings.buildings.camp_1.ui_helper
        else:
            building_location = city_map_location.troop_buildings.buildings.camp_2
            ui_helper_location = city_map_location.troop_buildings.buildings.camp_2.ui_helper
    elif building_type.lower() == 'factory':
        #  Recruit shredder only
        recruit_option = 1
        if number == 1:
            building_location = city_map_location.troop_buildings.buildings.factory_1
            ui_helper_location = city_map_location.troop_buildings.buildings.factory_1.ui_helper
        else:
            building_location = city_map_location.troop_buildings.buildings.factory_2
            ui_helper_location = city_map_location.troop_buildings.buildings.factory_2.ui_helper

    # Collect troops
    # handle_ui_helper_expand(vm_index)
    # vm.handle_tap(vm_index, ui_helper_location)

    # Recruit troops
    handle_ui_helper_expand(vm_index)
    vm.handle_tap(vm_index, ui_helper_location)
    vm.handle_tap(vm_index, functions_location.buildings.troop_buildings.recruit.select_recruit)


def handle_recruit_camp1(vm_index):
    handle_recruit_troop(vm_index, building_type='camp', number=1)


def handle_recruit_camp2(vm_index):
    handle_recruit_troop(vm_index, building_type='camp', number=2)


def handle_recruit_factory1(vm_index):
    handle_recruit_troop(vm_index, building_type='factory', number=1)


def handle_recruit_factory2(vm_index):
    handle_recruit_troop(vm_index, building_type='factory', number=2)


def handle_collect_farm(vm_index):
    handle_collect_resources(vm_index, city_map_location.resource_buildings.buildings.farm.coordinate)


def handle_collect_oil(vm_index):
    handle_collect_resources(vm_index, city_map_location.resource_buildings.buildings.oil_refinery.coordinate)


def handle_switch_account(vm_index, account_no):
    account = None
    total_accounts = len(functions_location.ui.my_info.account.functions.switch_account.accounts)
    if account_no in range(1, total_accounts):
        account = getattr(functions_location.ui.my_info.account.functions.switch_account.accounts, f"account_{account_no}")
    else:
        Exception("Invalid account: " + str(account_no))

    choose_email = account.choose_email
    choose_account = account.choose_account
    close_all_windows(vm_index)
    vm.handle_tap(vm_index, ui_location.my_info)
    vm.handle_tap(vm_index, functions_location.ui.my_info.account.coordinate)
    vm.handle_tap(vm_index, functions_location.ui.my_info.account.functions.switch_account.coordinate)
    vm.handle_tap(vm_index, functions_location.ui.my_info.account.functions.switch_account.game_login)
    time.sleep(5)
    vm.handle_tap(vm_index, choose_email)
    time.sleep(5)
    vm.handle_tap(vm_index, choose_account)
    vm.handle_tap(vm_index, functions_location.ui.my_info.account.functions.switch_account.confirm_choose_account)
    time.sleep(5)
    return account




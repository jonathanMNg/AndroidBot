import time
from object.coordinate import Coordinate
import vm


def switch_city_and_map(vm_index):
    vm.handle_touch(vm_index, 40, 615)
    time.sleep(3)


def close_all_windows(vm_index):
    vm.handle_return(vm_index)
    vm.handle_return(vm_index)
    vm.handle_touch(vm_index, 25, 105)


def go_to_city_view(vm_index):
    close_all_windows(vm_index)
    switch_city_and_map(vm_index)
    close_all_windows(vm_index)
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
    vm.handle_backspace(vm_index)
    vm.handle_enter(vm_index)
    for i in range(1, level):
        handle_select_add_button(vm_index)


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


def handle_gather_farm(vm_index):

    go_to_city_view(vm_index)
    switch_city_and_map(vm_index)

    handle_select_radar(vm_index)
    handle_select_farm(vm_index)
    handle_set_gather_resource_level(vm_index, 4)
    handle_select_go(vm_index)
    handle_select_resource_target(vm_index)
    handle_select_gather_icon(vm_index)
    handle_setout(vm_index)


def handle_gather_oil(vm_index):

    go_to_city_view(vm_index)
    switch_city_and_map(vm_index)

    handle_select_radar(vm_index)
    handle_select_oil_field(vm_index)
    handle_set_gather_resource_level(vm_index, 4)
    handle_select_go(vm_index)
    handle_select_resource_target(vm_index)
    handle_select_gather_icon(vm_index)
    handle_setout(vm_index)


def handle_select_collect_farm(vm_index):
    vm.handle_touch(vm_index, 145, 445)


def handle_select_collect_oil(vm_index):
    vm.handle_touch(vm_index, 185, 385)


def handle_collect_farm(vm_index):
    go_to_city_view(vm_index)
    vm.handle_swipe_horizontal(0, 200)
    vm.handle_swipe_vertical(0, -100)
    handle_select_collect_farm(vm_index)


def handle_collect_oil(vm_index):
    go_to_city_view(vm_index)
    vm.handle_swipe_horizontal(0, 200)
    vm.handle_swipe_vertical(0, -100)
    handle_select_collect_oil(vm_index)


def handle_select_recruit_camp_sniper(vm_index):
    vm.handle_touch(vm_index, 225, 475)


def handle_recruit_camp_recruit(vm_index):
    handle_select_recruit_camp_sniper(vm_index)
    vm.handle_touch(vm_index, 310, 625)


def handle_recruit_camp1(vm_index):
    go_to_city_view(vm_index)
    vm.handle_swipe_horizontal(vm_index, 100)
    vm.handle_touch(vm_index, 260, 450)
    vm.handle_touch(vm_index, 340, 480)
    handle_recruit_camp_recruit(vm_index)


def handle_recruit_camp2(vm_index):
    go_to_city_view(vm_index)
    vm.handle_swipe_horizontal(vm_index, 100)
    vm.handle_touch(vm_index, 190, 510)
    vm.handle_touch(vm_index, 270, 325)
    handle_recruit_camp_recruit(vm_index)


def handle_select_recruit_factory_shredder(vm_index):
    vm.handle_touch(vm_index, 165, 475)


def handle_recruit_factory_recruit(vm_index):
    handle_select_recruit_factory_shredder(vm_index)
    vm.handle_touch(vm_index, 310, 625)


def handle_recruit_factory1(vm_index):
    go_to_city_view(vm_index)
    vm.handle_swipe_horizontal(vm_index, 150)
    vm.handle_swipe_vertical(vm_index, -50)
    vm.handle_touch(vm_index, 180, 510)
    vm.handle_touch(vm_index, 270, 320)
    handle_recruit_factory_recruit(vm_index)

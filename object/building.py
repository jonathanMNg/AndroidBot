import vm
from locations.tap_path import TapPath
from object.coordinate import Coordinate
import time


class BuildingName(object):
    academy = 'academy'
    biochemical_lab = 'biochemical_lab'
    camp_1 = 'camp_1'
    camp_2 = 'camp_2'
    command_center = 'command_center'
    defense_tower = 'defense_tower'
    depot = 'depot'
    dispatch_center = 'dispatch_center'
    embassy = 'embassy'
    factory_1 = 'factory_1'
    factory_2 = 'factory_2'
    farm_1 = 'farm_1'
    garage = 'garage'
    house_1 = 'house_1'
    hospital = 'hospital'
    main_hall = 'main_hall'
    oil_1 = 'oil_1'
    recon_center = 'recon_center'
    steel_1 = 'steel_1'
    wall = 'wall'


class BuildingTapPath(object):
    academy = TapPath.Main_Hall
    biochemical_lab = TapPath.Main_Hall
    camp_1 = TapPath.Depot
    camp_2 = TapPath.Depot
    command_center = TapPath.Main_Hall
    defense_tower = TapPath.Lab_Wall_Tower
    depot = TapPath.Main_Hall
    dispatch_center = TapPath.Academy_Dispatch
    embassy = TapPath.Academy
    factory_1 = TapPath.Depot
    factory_2 = TapPath.Depot
    farm_1 = TapPath.Lab_Wall_Tower
    garage = TapPath.Lab
    house_1 = TapPath.Academy_Dispatch
    hospital = TapPath.Main_Hall
    main_hall = TapPath.Main_Hall
    oil_1 = TapPath.Lab_Wall_Tower
    recon_center = TapPath.Depot
    steel_1 = TapPath.Lab_Wall_Tower
    wall = TapPath.Lab


class BuildingCoordinate(object):
    academy = Coordinate(359, 330)
    biochemical_lab = Coordinate(157, 494)
    camp_1 = Coordinate(225, 445)
    camp_2 = Coordinate(165, 516)
    command_center = Coordinate(64, 404)
    defense_tower = Coordinate(200, 310)
    depot = Coordinate(317, 218)
    dispatch_center = Coordinate(192, 292)
    embassy = Coordinate(258, 324)
    factory_1 = Coordinate(300, 500)
    factory_2 = Coordinate(235, 544)
    farm_1 = Coordinate(209, 189)
    garage = Coordinate(48, 267)
    house_1 = Coordinate(208, 229)
    hospital = Coordinate(301, 396)
    main_hall = Coordinate(215, 285)
    oil_1 = Coordinate(254, 149)
    recon_center = Coordinate(290, 168)
    steel_1 = Coordinate(237, 357)
    wall = Coordinate(303, 399)


class BuildingFunctions:
    def __init__(self, building_name, vm_index):
        self.building_name = building_name
        self.vm_index = vm_index

    def navigate_to_building(self):
        tap_path = getattr(BuildingTapPath, self.building_name)
        for coordinate in tap_path:
            vm.handle_tap(self.vm_index, coordinate)

    def tap_on_building(self):
        building_coordinate = getattr(BuildingCoordinate, self.building_name)
        vm.handle_tap(self.vm_index, building_coordinate)

    def upgrade(self):
        upgrade_coordinate = Coordinate(0, 0)
        if self.building_name == BuildingName.main_hall:
            upgrade_coordinate = Coordinate(143, 313)
        elif self.building_name == BuildingName.hospital:
            upgrade_coordinate = Coordinate(300, 471)
        elif self.building_name == BuildingName.depot:
            upgrade_coordinate = Coordinate(195, 300)
        elif self.building_name == BuildingName.embassy:
            upgrade_coordinate = Coordinate(197, 376)
        elif self.building_name == BuildingName.academy:
            upgrade_coordinate = Coordinate(196, 344)
        elif self.building_name == BuildingName.garage:
            upgrade_coordinate = Coordinate(156, 358)
        elif self.building_name == BuildingName.farm_1:
            upgrade_coordinate = Coordinate(240, 243)
        elif self.building_name == BuildingName.oil_1:
            upgrade_coordinate = Coordinate(228, 350)
        elif self.building_name == BuildingName.camp_1:
            upgrade_coordinate = Coordinate(225, 517)
        elif self.building_name == BuildingName.camp_2:
            upgrade_coordinate = Coordinate(194, 362)
        elif self.building_name == BuildingName.factory_1:
            upgrade_coordinate = Coordinate(195, 363)
        elif self.building_name == BuildingName.factory_2:
            upgrade_coordinate = Coordinate(195, 365)
        elif self.building_name == BuildingName.recon_center:
            upgrade_coordinate = Coordinate(194, 237)
        elif self.building_name == BuildingName.house_1:
            upgrade_coordinate = Coordinate(239, 285)
        elif self.building_name == BuildingName.dispatch_center:
            upgrade_coordinate = Coordinate(237, 355)
        elif self.building_name == BuildingName.wall:
            upgrade_coordinate = Coordinate(158, 367)
        elif self.building_name == BuildingName.steel_1:
            upgrade_coordinate = Coordinate(272, 424)

        self.navigate_to_building()
        self.tap_on_building()
        # print(upgrade_coordinate.x, upgrade_coordinate.y)
        vm.handle_tap(self.vm_index, upgrade_coordinate)
        # Tap on upgrade
        vm.handle_tap(self.vm_index, Coordinate(307, 622))


class Building:
    def __init__(self, building_name, vm_index):
        self.building_name = building_name
        self.vm_index = vm_index

    def upgrade(self):
        my_building = BuildingFunctions(self.building_name, self.vm_index)
        my_building.upgrade()


from object.coordinate import Coordinate
from object.building import BuildingName
functions = {
    'buildings': {
        'functions': {
          'upgrade': Coordinate(305, 625)
        },
        'special_buildings': {

        },
        'troop_buildings': {
            'collect_troop': None,
            'recruit': {
                'select_option_1': Coordinate(165, 475),
                'select_option_2': Coordinate(220, 480),
                'select_recruit': Coordinate(305, 625)
            }
        }
    },
    'tab_bar': {
        'my_info': {
            'account': {
                'coordinate': Coordinate(320, 600),
                'functions': {
                    'switch_account': {
                        'coordinate': Coordinate(200, 495),
                        'game_login': Coordinate(200, 356),
                        'confirm_choose_account': Coordinate(125, 360)
                    },
                }
            }

        }
    },
    'map_view': {
        'gather': {
            'functions': {
                'radar': Coordinate(370, 515),
                'go': Coordinate(345, 602),
                'gather': Coordinate(274, 293),
                'set_out': Coordinate(330, 620)
            },
            'select_resource_type': {
                'farm': Coordinate(48, 527),
                'oil': Coordinate(110, 527),
                'steel': Coordinate(165, 527),
                'mineral': Coordinate(225, 527)
            }
        }
    }
}

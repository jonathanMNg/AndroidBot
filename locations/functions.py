from object.coordinate import Coordinate

functions = {
    'buildings': {
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
    'ui': {
        'my_info': {
            'account': {
                'coordinate': Coordinate(320, 600),
                'functions': {
                    'switch_account': {
                        'coordinate': Coordinate(200, 495),
                        'accounts': {
                            'account_1': {
                                'choose_email': Coordinate(190, 330),
                                'choose_account': Coordinate(200, 245),
                                'level': 15
                            },
                            'account_2': {
                                'choose_email': Coordinate(190, 330),
                                'choose_account': Coordinate(200, 285),
                                'level': 10
                            },
                            'account_3': {
                                'choose_email': Coordinate(190, 375),
                                'choose_account': Coordinate(200, 245),
                                'level': 10
                            },
                            'account_4': {
                                'choose_email': Coordinate(190, 375),
                                'choose_account': Coordinate(200, 285),
                                'level': 10

                            },
                            'account_5': {
                                'choose_email': Coordinate(190, 420),
                                'choose_account': Coordinate(200, 245),
                                'level': 10

                            },
                            'account_6': {
                                'choose_email': Coordinate(190, 420),
                                'choose_account': Coordinate(200, 285),
                                'level': 10

                            }
                        },
                        'game_login': Coordinate(200, 356),
                        'confirm_choose_account': Coordinate(125, 360)
                    },
                }
            }

        }
    }
}

from object.coordinate import Coordinate

city_map = {
    'special_buildings': {
        'direction_from_default_view': {
            'horizontal': -150,
            'vertical': -100
        },
        'buildings': {
            'garage': {
                'coordinate': Coordinate(190, 310),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(150, 395)
                    }
                }
            },
            'command_center': {
                'coordinate': Coordinate(250, 275),
                'functions': {
                    'recruit_officers': {
                        'coordinate': Coordinate(330, 305)
                    },
                }
            },
            'city_hall': {
                'coordinate': Coordinate(300, 230),
                'functions': {
                    'daily_reward': {
                        'coordinate': Coordinate(215, 255)
                    },
                }
            },
            'biochemical_lab': {
                'coordinate': Coordinate(355, 345),
                'functions': {
                    'treatment_room': {
                        'coordinate': Coordinate(155, 360)
                    },
                }
            },
            'manage_troops': {
                'coordinate': Coordinate(335, 470),
                'functions': {
                    'promote_troops': {
                        'coordinate': Coordinate(230, 360)
                    },
                }
            },
        }
    },
    'troop_buildings': {
        'direction_from_default_view': {
            'horizontal': 150,
            'vertical': -100
        },
        'buildings': {
            'camp_1': {
                'coordinate': Coordinate(190, 300),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(280, 350)
                    }
                }
            },
            'camp_2': {
                'coordinate': Coordinate(225, 360),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(225, 410)
                    }
                }
            },
            'factory_1': {
                'coordinate': Coordinate(250, 345),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(255, 345)
                    }
                }
            },
            'factory_2': {
                'coordinate': Coordinate(195, 400),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(285, 460)
                    }
                }
            },
            'embassy': {
                'coordinate': Coordinate(240, 300),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(175, 355)
                    }
                }
            },
        },
    },
    'resource_buildings': {
        'direction_from_default_view': {
            'horizontal': 300,
            'vertical': -150
        },
        'buildings': {
            'oil_refinery': {
                'coordinate': Coordinate(205, 265),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(240, 325)
                    }
                }
            },
            'farm': {
                'coordinate': Coordinate(155, 315),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(187, 380)
                    }
                }
            },
        },
    },
    'development_buildings': {
        'direction_from_default_view': {
            'horizontal': 0,
            'vertical': 0
        },
        'buildings': {
            'main_hall': {
                'coordinate': Coordinate(215, 300),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(140, 310)
                    }
                }
            },
            'academy': {
                'coordinate': Coordinate(365, 350),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(285, 355)
                    }
                }
            },
        }
    }
}

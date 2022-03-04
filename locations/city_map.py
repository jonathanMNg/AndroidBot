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
            'horizontal': 120,
            'vertical': -100
        },
        'buildings': {
            'camp_1': {
                'coordinate': Coordinate(215, 265),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(305, 340)
                    }
                },
                'ui_helper': Coordinate(40, 140)
            },
            'camp_2': {
                'coordinate': Coordinate(165, 345),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(240, 375)
                    }
                },
                'ui_helper': Coordinate(120, 140)
            },
            'factory_1': {
                'coordinate': Coordinate(280, 330),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(370, 390)
                    }
                },
                'ui_helper': Coordinate(200, 140)
            },
            'factory_2': {
                'coordinate': Coordinate(220, 380),
                'functions': {
                    'recruit': {
                        'coordinate': Coordinate(315, 435)
                    }
                },
                'ui_helper': Coordinate(40, 220)
            },
            'embassy': {
                'coordinate': Coordinate(260, 230),
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
                'coordinate': Coordinate(269, 241),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(240, 325)
                    }
                }
            },
            'farm': {
                'coordinate': Coordinate(212, 290),
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

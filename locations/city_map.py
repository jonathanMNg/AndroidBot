from object.coordinate import Coordinate

city_map = {
    'special_buildings': {
        'tap_path_from_default_view': [
            Coordinate(60, 409)
        ],
        'buildings': {
            'garage': {
                'coordinate': Coordinate(141, 324),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(90, 415)
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
        'tap_path_from_default_view': [
            Coordinate(189, 230), Coordinate(300, 403)
        ],
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
                'coordinate': Coordinate(300, 133),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(283, 381)
                    }
                }
            },
            'recon_center': {
                'coordinate': Coordinate(288, 168),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(193, 235)
                    }
                }
            },
        },
    },
    'resource_buildings': {
        'tap_path_from_default_view': [
            Coordinate(155, 513), Coordinate(300, 403), Coordinate(335, 435), Coordinate(90, 300)
        ],
        'buildings': {
            'oil': {
                'coordinate': Coordinate(255, 146),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(225, 350)
                    }
                }
            },
            'farm': {
                'coordinate': Coordinate(205, 186),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(240, 240)
                    }
                }
            },
            'steel': {
                'coordinate': Coordinate(237, 413),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(187, 380)
                    }
                }
            },
            'mineral': {
                'coordinate': Coordinate(327, 419),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(228, 475)
                    }
                }
            }
        },
    },
    'development_buildings': {
        'tap_path_from_default_view': [

        ],
        'buildings': {
            'main_hall': {
                'coordinate': Coordinate(215, 280),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(140, 310)
                    }
                }
            },
            'academy': {
                'coordinate': Coordinate(360, 330),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(195, 343)
                    },
                    'research': {
                        'coordinate': Coordinate(270, 315)
                    }
                }
            },
            'hospital': {
                'coordinate': Coordinate(300, 415),
                'functions': {
                    'upgrade': {
                        'coordinate': Coordinate(300, 470)
                    }
                }
            }
        }
    }
}

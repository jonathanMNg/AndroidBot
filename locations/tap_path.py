from object.coordinate import Coordinate
from enum import Enum


class TapPath:
    # Patter [location 1, location 2, ...location x, empty space to clear out the ui]
    Lab_Wall_Tower = [
        Coordinate(155, 513), Coordinate(300, 403), Coordinate(335, 435), Coordinate(51, 294)
    ]
    Lab = [
        Coordinate(152, 493), Coordinate(212, 495)
    ]
    Depot = [
        Coordinate(315, 222), Coordinate(150, 135)
    ]
    Main_Hall = [

    ]
    Academy = [
        Coordinate(360, 329), Coordinate(284, 210)
    ]
    Academy_Dispatch = [
        Coordinate(360, 329), Coordinate(370, 319), Coordinate(229, 459)
    ]


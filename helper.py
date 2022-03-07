from locations import city_map_location


def get_building_information(object_str):
    object_split = object_str.split('.')
    obj = city_map_location
    for str in object_split:
        obj = getattr(obj, str)
    return obj

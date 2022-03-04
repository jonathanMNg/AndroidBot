from locations.city_map import city_map
from locations.ui import ui
from locations.functions import functions
from munch import munchify

city_map_location = munchify(city_map)
ui_location = munchify(ui)
functions_location = munchify(functions)

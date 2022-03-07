from locations import city_map_location
import datetime
import time
starting_minute = datetime.datetime.now().minute
current_minute = datetime.datetime.now().minute
interval_minute = 1

while True:
    current_minute = datetime.datetime.now().minute
    print("hello world!")
    if current_minute > starting_minute:
        print("do something")
        starting_minute = current_minute

    time.sleep(10)

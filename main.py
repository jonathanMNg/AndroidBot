import time
import datetime
import vm
import game
from keyboard import keyboard
from object.coordinate import Coordinate
if __name__ == "__main__":

    #vm.start_vm('MEmu2', 0)
    #vm.stop_vm('Memu2', 0)
    #vm.start_game(0)

    vm.handle_swipe_horizontal(0, 300)
    vm.handle_swipe_vertical(0, -150)
    # while True:
    #     Collect Resources
    #     game.handle_collect_oil(0)
    #     game.handle_collect_farm(0)
    #
    #     #  Gather Resources
    #     game.handle_gather_oil(0)
    #
    #     #  Recruit Camp
    #     game.handle_recruit_camp1(0)
    #     game.handle_recruit_camp2(0)
    #
    #     #  Recruit Factory
    #     game.handle_recruit_factory1(0)
    #     #  Wait for 30 minutes
    #     print("sleeping..." + str(datetime.datetime.now().time()))
    #     time.sleep(60)

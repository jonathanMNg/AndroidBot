import time
from object.coordinate import Coordinate
import win32con
import win32gui
import subprocess
from keyboard import keyboard

memu = 'C:\\Program Files\\Microvirt\\MEmu\\memuc.exe'
game_identifier = 'com.camelgames.aoz'


# A detailed explanation of find_window function is below.
def find_window(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        return False
    else:
        return True


def start_vm(vm_name,vm_index):
    cmd = f"{memu} start -i {vm_index}"
    try:
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        result, output = vm.stdout.split(':')

        print(result)
        print(output)
        if result == 'ERROR':
            print('Memu returned Error. Switching to Manual Confirmation')
            if find_window(window_title=vm_name):
                return True
            else:
                return False
        elif result == 'SUCCESS':
            print('Command Success')
            return True
        else:
            print('Unknown error')
            return False

    except Exception:
        raise


def force_close_window(window_title):
    handle = win32gui.FindWindow(None, window_title)
    result = win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)
    time.sleep(1)
    hwnd = find_window(window_title)
    if not hwnd:
        return True
    elif hwnd:
        return False


def stop_vm(window_title, vm_index):
    cmd = f"{memu} stop vm -i {vm_index}"
    vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')

    time.sleep(1)
    is_running = find_window(f"({window_title})")
    if is_running:
        # Check if window is still opened after executing the stop vm command. If True close the window manually.
        force_close = force_close_window(window_title)
        if force_close:
            return True

        elif not force_close:
            raise Exception("Failed to close VM")

    elif not is_running:
        return True


def reboot_vm(vm_index):
    cmd = f"{memu} reboot vm -i {vm_index}"
    handle_run_command(vm_index, cmd)


def verify_game_process(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell pidof {game_identifier}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        output = proc.stdout.splitlines()[2]
        print(f" Android Process ID = {int(output)}")
        return int(output)

    except Exception:
        return False


def is_game_open(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell dumpsys window windows | grep mCurrentFocus"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        output = proc.stdout.splitlines()[2]
        if game_identifier in output:
            return True
        else:
            return False

    except Exception:
        return False


def start_game(vm_index):
    try:
        cmd = f"{memu} startapp -i {vm_index} {game_identifier}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        output, result = proc.stdout.split(":")
        print(result)
        print(output)
        time.sleep(5)
        result = verify_game_process(vm_index)
        if isinstance(result, int):

            print(output)
            return True
    except Exception:
        raise


def handle_restart_if_game_not_open(vm_index):
    if not is_game_open(vm_index):
        stop_vm("", vm_index)
        time.sleep(5)
        start_vm("", vm_index)
        time.sleep(10)
        start_game(vm_index)
        time.sleep(10)


def handle_touch(vm_index, x, y):
    cmd = f"{memu} -i {vm_index} adb shell input tap {x} {y}"
    handle_run_command(vm_index, cmd)


def handle_tap(vm_index, coordinate):
    cmd = f"{memu} -i {vm_index} adb shell input tap {coordinate.x} {coordinate.y}"
    handle_run_command(vm_index, cmd)


def handle_return(vm_index):
    cmd = f"{memu} -i {vm_index} adb shell input keyevent 4"
    handle_run_command(vm_index, cmd)


def handle_backspace(vm_index):
    time.sleep(1)
    cmd = f"{memu} -i {vm_index} adb shell input keyevent 67"
    handle_run_command(vm_index, cmd)


def handle_enter(vm_index):
    cmd = f"{memu} -i {vm_index} adb shell input keyevent 66"
    handle_run_command(vm_index, cmd)


def handle_input(vm_index, key):
    keycode = keyboard[str(key)]
    cmd = f"{memu} -i {vm_index} adb shell input keyevent {keycode}"
    handle_run_command(vm_index, cmd)


def handle_swipe(vm_index, src_coor, dest_coor):

    cmd = f"{memu} -i {vm_index} adb shell input swipe {src_coor.x} {src_coor.y} {dest_coor.x} {dest_coor.y}"
    handle_run_command(vm_index, cmd)


def handle_long_tap(vm_index, coordinate):
    cmd = f"{memu} -i {vm_index} adb shell input swipe {coordinate.x} {coordinate.y} {coordinate.x} {coordinate.y} 1000"
    handle_run_command(vm_index, cmd)


def handle_run_command(vm_index, command):
    time.sleep(1)
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False


def handle_swipe_vertical(vm_index, distance):
    minY = 0
    maxY = 640
    src_coor = Coordinate(200, 300)  # center coordinate
    dest_coor = Coordinate(200, 300)
    dest_coor.y = dest_coor.y + distance
    if dest_coor.y < minY:
        dest_coor.y = minY
    elif dest_coor.y > maxY:
        dest_coor.y = maxY
    handle_swipe(vm_index, src_coor, dest_coor)


def handle_swipe_horizontal(vm_index, distance):
    minX = 0
    maxX = 400
    src_coor = Coordinate(200, 300)  # center coordinate
    dest_coor = Coordinate(200, 300)
    dest_coor.x = dest_coor.x - distance
    if dest_coor.x < minX:
        dest_coor.x = minX
    elif dest_coor.x > maxX:
        dest_coor.x = maxX
    handle_swipe(vm_index, src_coor, dest_coor)


def handle_swipe_to_location(vm_index, horizontal_distance, vertical_distance):
    handle_swipe_horizontal(vm_index, horizontal_distance)
    handle_swipe_vertical(vm_index, vertical_distance)


def handle_screen_shot(vm_index):
    time.sleep(1)
    try:
        cmd = f"{memu} -i {vm_index} adb shell screencap -p /sdcard/screen.png"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        cmd = f"{memu} -i {vm_index} adb pull /sdcard/screen.png ./screen.png"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False

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
        print(vm)
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
    result = win32gui.PostMessage(handle, win32con.WM_CLOSE,0,0)
    time.sleep(1)
    hwnd = find_window(window_title)
    if not hwnd:
        return True
    elif hwnd:
        return False

def stop_vm(window_title,vm_index):
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

def verify_game_process(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell pidof {game_identifier}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        output = proc.stdout.splitlines()[2]
        print(f" Android Process ID = {int(output)}")
        return int(output)

    except Exception:
        return False

def start_game(vm_index):
    try:
        cmd = f"{memu} startapp -i {vm_index} {game_identifier}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        output, result = proc.stdout.split(":")
        time.sleep(5)
        result = verify_game_process(vm_index)
        if isinstance(result, int):

            print(output)
            return True
    except Exception:
        raise


def handle_touch(vm_index, x, y):
    try:
        cmd = f"{memu} -i {vm_index} adb shell input tap {x} {y}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        time.sleep(1)
        # output = proc.stdout.splitlines()[2]
    except Exception:
        return False


def handle_tap(vm_index, coordinate):
    try:
        cmd = f"{memu} -i {vm_index} adb shell input tap {coordinate.x} {coordinate.y}"
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        time.sleep(1)
    except Exception:
        return False


def handle_return(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell input keyevent 4"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False


def handle_backspace(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell input keyevent 67"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False


def handle_enter(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell input keyevent 66"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False


def handle_input(vm_index, key):
    keycode = keyboard[str(key)]
    try:
        cmd = f"{memu} -i {vm_index} adb shell input keyevent {keycode}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False


def handle_swipe(vm_index, src_coor, dest_coor):
    try:
        cmd = f"{memu} -i {vm_index} adb shell input swipe {src_coor.x} {src_coor.y} {dest_coor.x} {dest_coor.y}"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        return False


def handle_swipe_vertical(vm_index, distance):
    minY = 0
    maxY = 640
    src_coor = Coordinate(200, 320)  # center coordinate
    dest_coor = Coordinate(200, 320)
    dest_coor.y = dest_coor.y + distance
    if dest_coor.y < minY:
        dest_coor.y = minY
    elif dest_coor.y > maxY:
        dest_coor.y = maxY
    handle_swipe(vm_index, src_coor, dest_coor)


def handle_swipe_horizontal(vm_index, distance):
    minX = 0
    maxX = 400
    src_coor = Coordinate(200, 320)  # center coordinate
    dest_coor = Coordinate(200, 320)
    dest_coor.x = dest_coor.x - distance
    if dest_coor.x < minX:
        dest_coor.x = minX
    elif dest_coor.x > maxX:
        dest_coor.x = maxX
    handle_swipe(vm_index, src_coor, dest_coor)

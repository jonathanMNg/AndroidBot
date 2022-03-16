import time
from object.coordinate import Coordinate
import win32con
import win32gui
import subprocess
from keyboard import keyboard

memu = 'C:\\Program Files\\Microvirt\\MEmu\\memuc.exe'
game_identifier = 'com.camelgames.aoz'


def run_memuc(cmd):
    try:
        cmd = f"{memu} {cmd}"
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        print(vm.stdout)
    except Exception:
        print(Exception)


def is_vm_running(vm_index):
    try:
        cmd = f"{memu} isvmrunning -i {vm_index}"
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        if 'Not Running' in vm.stdout:
            return False
        else:
            return True
    except Exception:
        raise


def start_vm(vm_index):
    try:
        cmd = f"{memu} start -i {vm_index}"
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        result = vm.stdout

        if 'ERROR' in result:
            print('Error starting vm')
            return 0
        elif 'SUCCESS' in result:
            print('Command Success')
            pid = get_vm_pid(vm_index)
            return pid
        else:
            print('Unknown error starting vm')
            print(result)
            return 0

    except Exception:
        raise


def force_close_window(pid):
    try:
        cmd = f"taskkill /F /PID {pid}"
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
    except Exception:
        raise


def get_vm_pid(vm_index):
    try:
        cmd = f"{memu} listvms -i {vm_index}"
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        v_index, v_title, v_window_handle, v_status, v_pid = vm.stdout.split(',')
        return v_pid.strip()
    except Exception:
        return False


def stop_vm(vm_index, pid):
    try:
        cmd = f"{memu} stop vm -i {vm_index}"
        vm = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        time.sleep(1)
        if is_vm_running(vm_index):
            force_close_window(pid)
            time.sleep(1)
    except Exception:
        raise


def reboot_vm(vm_index):
    cmd = f"{memu} reboot vm -i {vm_index}"
    handle_run_command(vm_index, cmd)


# def verify_game_process(vm_index):
#     try:
#         cmd = f"{memu} -i {vm_index} adb shell pidof {game_identifier}"
#         proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
#         output = proc.stdout.splitlines()[2]
#         print(f" Android Process ID = {int(output)}")
#         return int(output)
#
#     except Exception:
#         return False


def is_game_open(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell dumpsys window windows | grep mCurrentFocus"
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        output = proc.stdout
        if game_identifier in output:
            return True
        else:
            return False
    except Exception:
        return False


def start_game(vm_index):
    if is_vm_running(vm_index):
        try:
            cmd = f"{memu} startapp -i {vm_index} {game_identifier}"
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
            time.sleep(5)
        except Exception:
            raise
    else:
        print("Error: vm is not running!")


def kill_app(vm_index):
    try:
        cmd = f"{memu} -i {vm_index} adb shell am force-stop {game_identifier}"
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding='utf-8')
        time.sleep(2)
    except Exception:
        raise


def handle_if_game_not_open(vm_index, pid):
    if not is_vm_running(vm_index):
        pid = start_vm(vm_index)
        time.sleep(10)
    else:
        pid = pid
    if not is_game_open(vm_index):
        kill_app(vm_index)
        time.sleep(1)
        start_game(vm_index)
        time.sleep(5)
        if not is_game_open(vm_index):
            stop_vm(vm_index, pid)
            time.sleep(3)
            pid = handle_if_game_not_open(vm_index, pid)
    return pid


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

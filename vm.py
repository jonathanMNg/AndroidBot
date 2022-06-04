import time
import subprocess
import keyboard
memu = '"C:\\Program Files\\Microvirt\\MEmu\\memuc.exe"'
game_identifier = 'com.camelgames.aoz'


def is_vm_running(vm_index, vm_title):
    cmd = f"{memu} isvmrunning -i {vm_index}"
    try:
        vm = handle_run_command(cmd, isshell=True)
        if 'NOT RUNNING' in vm.stdout.upper():
            return False
        else:
            return True
    except Exception as err:
        return False


def count_tasks(task_name):
    cmd = f"tasklist | find \"{task_name}\""

    try:
        vm = handle_run_command(cmd, isshell=True)
        if vm.stdout == '':
            return 0
        else:
            count = len(vm.stdout.strip().split('\n'))
            return count
    except Exception:
        return 0


def is_vm_window_open(vm_title):
    cmd = f"tasklist /FI \"WINDOWTITLE eq ({vm_title})\" | find \"MEmu.exe\""
    try:
        vm = handle_run_command(cmd, isshell=True)
        if vm.stdout == '':
            return False
        else:
            return True
    except Exception:
        return False


def start_vm(vm_index):
    cmd = f"{memu} start -i {vm_index}"
    vm = handle_run_command(cmd)
    time.sleep(2)
    result = vm.stdout

    if 'ERROR' in result.upper():
        print("Error: " + result)
        return False
    elif 'SUCCESS' in result.upper():
        print('Command Success')
        return True
    else:
        print(result)
        return False


def force_close_window(vm_title):
    cmd = f"taskkill /F /FI \"WINDOWTITLE eq ({vm_title})\""
    handle_run_command(cmd)


# def get_vm_pid(vm_index):
#     cmd = f"{memu} listvms -i {vm_index}"
#     vm = handle_run_command(cmd)
#     v_index, v_title, v_window_handle, v_status, v_pid = vm.stdout.split(',')
#     return v_pid.strip()


def stop_vm(vm_index, vm_title):

    if is_vm_running(vm_index, vm_title):
        cmd = f"{memu} stop vm -i {vm_index}"
        handle_run_command(cmd)
        time.sleep(3)

    if is_vm_window_open(vm_title):
        force_close_window(vm_title)
        time.sleep(3)
        stop_vm(vm_index, vm_title)


def is_game_open(vm_index):
    cmd = f"{memu} -i {vm_index} adb shell dumpsys window windows | grep mCurrentFocus"
    proc = handle_run_command(cmd, True)
    output = proc.stdout
    if game_identifier in output:
        return True
    else:
        return False


def start_game(vm_index, vm_title):
    if is_vm_running(vm_index, vm_title):
        cmd = f"{memu} startapp -i {vm_index} {game_identifier}"
        handle_run_command(cmd)
    else:
        print("Error: vm is not running!")


def kill_app(vm_index):
    cmd = f"{memu} -i {vm_index} adb shell am force-stop {game_identifier}"
    handle_run_command(cmd)


def restart_app(vm_index, vm_title):
    kill_app(vm_index)
    time.sleep(2)
    start_game(vm_index, vm_title)
    time.sleep(10)


def handle_if_game_not_open(vm_index, vm_title):
    if not is_vm_running(vm_index, vm_title):
        if is_vm_window_open(vm_title):
            force_close_window(vm_title)
            time.sleep(2)
        start_vm(vm_index)
        time.sleep(20)
        return handle_if_game_not_open(vm_index, vm_title)

    if not is_game_open(vm_index):
        kill_app(vm_index)
        time.sleep(3)
        start_game(vm_index, vm_title)
        time.sleep(30)
        if not is_game_open(vm_index):
            stop_vm(vm_index, vm_title)
            time.sleep(3)
            return handle_if_game_not_open(vm_index, vm_title)
        return True
    return False


def handle_tap(vm_index, coordinate):
    cmd = f"{memu} -i {vm_index} adb shell input tap {coordinate.x} {coordinate.y}"
    handle_run_command(cmd, vm_index, f"AOZ_{vm_index}")


def handle_return(vm_index):
    cmd = f"{memu} -i {vm_index} adb shell input keyevent 4"
    handle_run_command(cmd)


def handle_enter(vm_index):
    cmd = f"{memu} -i {vm_index} adb shell input keyevent 66"
    handle_run_command(cmd)


def handle_input(vm_index, key):
    keycode = keyboard[str(key)]
    cmd = f"{memu} -i {vm_index} adb shell input keyevent {keycode}"
    handle_run_command(cmd)


def handle_long_tap(vm_index, coordinate):
    cmd = f"{memu} -i {vm_index} adb shell input swipe {coordinate.x} {coordinate.y} {coordinate.x} {coordinate.y} 1000"
    handle_run_command(cmd)


def handle_run_command(command, vm_index=-1, vm_title='', isshell=False):
    time.sleep(1)
    try:
        vm = subprocess.run(command, check=True, stdout=subprocess.PIPE, encoding='utf-8', shell=isshell, stderr=subprocess.PIPE)
        if vm.stdout == '' or vm.stderr != '':
            if vm_index != -1 and vm_title != '':
                handle_if_game_not_open(vm_index, vm_title)
                vm = handle_run_command(command, vm_index, vm_title, isshell=True)
        return vm
    except Exception:
        raise


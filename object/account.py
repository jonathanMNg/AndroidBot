from object.coordinate import Coordinate
import vm
import game
from locations import ui_location, functions_location
import time


class Account:
    def __init__(self, name, level, target_upgrade='', target_research=''):
        self.level = level
        self.name = name
        self.target_upgrade = target_upgrade
        self.target_research = target_research


class EmailAccount:
    def __init__(self, email_accounts=[]):
        self.email_accounts = email_accounts

    def add(self, email_account):
        self.email_accounts.append(email_account)

    def get_total_accounts(self):
        return len(self.email_accounts)

    def get_all(self):
        return self.email_accounts

    def clear(self):
        self.email_accounts.clear()


class Accounts:
    def __init__(self, vm_index, email_accounts=[]):
        self.email_accounts = email_accounts
        self.vm_index = vm_index

    def add(self, email_account):
        self.email_accounts.append(email_account)

    def get_total_accounts(self):
        return len(self.email_accounts)

    def get_all(self):
        return self.email_accounts

    def switch_account(self, email_order, account_order):
        email_starting_x = 170
        email_starting_y = 0
        account_starting_x = 200
        account_starting_y = 245
        email_distance_y = 50
        account_distance_y = 40
        if self.get_total_accounts() == 1:
            email_starting_y = 380
        elif self.get_total_accounts() == 2:
            email_starting_y = 355
        elif self.get_total_accounts() == 3:
            email_starting_y = 330
        elif self.get_total_accounts() == 4:
            email_starting_y = 305

        # email_accounts = self.email_accounts[email_order]
        # account = email_accounts.get_all()[account_order]
        choose_email = Coordinate(email_starting_x, (email_starting_y + email_distance_y * (email_order)))
        choose_account = Coordinate(account_starting_x, (account_starting_y + account_distance_y * (account_order)))
        game.close_all_windows(self.vm_index)
        vm.handle_tap(self.vm_index, ui_location.my_info)
        vm.handle_tap(self.vm_index, functions_location.tab_bar.my_info.account.coordinate)
        vm.handle_tap(self.vm_index, functions_location.tab_bar.my_info.account.functions.switch_account.coordinate)
        vm.handle_tap(self.vm_index, functions_location.tab_bar.my_info.account.functions.switch_account.game_login)
        time.sleep(5)
        vm.handle_tap(self.vm_index, choose_email)
        time.sleep(5)
        vm.handle_tap(self.vm_index, choose_account)
        vm.handle_tap(self.vm_index, functions_location.tab_bar.my_info.account.functions.switch_account.confirm_choose_account)
        time.sleep(5)


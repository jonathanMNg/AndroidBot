from object.account import *

email_accounts_1 = [
    Account('ChoppaPopa', 10)
]

email_accounts_2 = [
    Account('Commander123', 9)
]

accounts = Accounts([email_accounts_1, email_accounts_2])

print(accounts.get_total_accounts())

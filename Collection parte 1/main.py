from banco import CheckingAccount, SavingAccount, InvestimentAccount
from operator import attrgetter

maria_account = CheckingAccount(112834)
maria_account.deposit(500)
maria_account.next_month()

guilherme_account = SavingAccount(218742)
guilherme_account.deposit(500)
guilherme_account.next_month()

deborah_account = CheckingAccount(112834)

accounts = [maria_account, guilherme_account]
for account in accounts:
    print(account)

#julia_accounts = InvestimentAccount(34)

print(maria_account == deborah_account)
accounts.append(deborah_account)

for account in sorted(accounts, key=attrgetter("balance")):
    print(account)

for account in sorted(accounts, reverse=True):
    print(account)
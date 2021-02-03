from banco import CheckingAccount, SavingAccount, InvestimentAccount
from operator import attrgetter

maria_account = CheckingAccount(112834)
maria_account.deposit(500)

guilherme_account = SavingAccount(218742)
guilherme_account.deposit(500)

deborah_account = CheckingAccount(236819)
deborah_account.deposit(300)

accounts = [guilherme_account, maria_account]
for account in accounts:
    print(account)

#julia_accounts = InvestimentAccount(34)

print(maria_account == deborah_account)
accounts.append(deborah_account)

for account in sorted(accounts, key=attrgetter("balance")):
    print(account)
print("\n")

for account in sorted(accounts, key=attrgetter("balance", "code")):
    print(account)
print("\n")

for account in sorted(accounts):
    print(account)
print("\n")

for account in sorted(accounts, reverse=True):
    print(account)
print("\n")

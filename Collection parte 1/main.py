from banco import CheckingAccount, SavingAccount, InvestimentAccount

maria_account = CheckingAccount(112834)
maria_account.deposit(500)
maria_account.next_month()

guilherme_account = SavingAccount(218742)
guilherme_account.deposit(500)
guilherme_account.next_month()

accounts = [maria_account, guilherme_account]
for account in accounts:
    print(account)


julia_accounts = InvestimentAccount(34)

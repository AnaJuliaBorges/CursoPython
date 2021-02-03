from banco import ContaCorrente

conta_da_maria = ContaCorrente(112834)
conta_da_maria.deposit(289)

conta_do_guilherme = ContaCorrente(218742)
conta_do_guilherme.deposit(30)

accounts = [conta_do_guilherme, conta_da_maria]
for account in accounts:
    print(account)
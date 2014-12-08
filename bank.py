class Bank(object): 
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):#pragma:nocover
        return self.accounts.get(account_number)

    def withdraw_from(self, account_number, amount):
        if type(amount) == int:
            if self.accounts.get(account_number) - amount >= 0:
                return self.accounts.get(account_number) - amount
            else:
                return 'Insufficient Funds'
        else:
            raise TypeError("Invalid type: {}".format(type(amount)))

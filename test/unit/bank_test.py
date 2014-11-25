import unittest
from account import Account
from bank import Bank

class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_is_initially_empty(self):
        self.assertEqual({}, self.bank.accounts)
        self.assertEqual(len(self.bank.accounts),0)
    
    def test_add_account(self):

        account_1 = Account("001",50)
        account_2 = Account("002", 100)
        
        self.bank.add_account(account_1)
        self.bank.add_account(account_2)
   
        self.assertEqual(len(self.bank.accounts),2)

    def test_get_account_balance(self):
        
        account_1 = Account("001", 50)

        self.bank.add_account(account_1)

        self.assertEqual(self.bank.get_account_balance("001"), 50)

    def test_withdraw_from_account(self):

        account_2 = Account("002", 100)

        self.bank.add_account(account_2)

        self.assertEqual(self.bank.withdraw_from("002", 50), 50)
        
    def test_withdraw_from_method_raises_typeerror_if_not_ints(self):
        
        account_2 = Account("002", 100)
        
        self.bank.add_account(account_2)

        self.assertRaises(TypeError, self.bank.withdraw_from, "002", "50")

    def test_account_does_not_exists(self):
        
        self.assertIn(Account("003",20),self.bank.accounts)

    def test_withdraw_from_method_insufficient_amount(self):

        account_2 = Account("002", 100)

        self.bank.add_account(account_2)

        self.assertEqual(self.bank.withdraw_from("002", 120), 'Insufficient Funds') 
  
if __name__ == '__main__':
    unittest.main()


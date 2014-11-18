import unittest
from account import Account
from bank import Bank

class BankTest(unittest.TestCase):
    def test_bank_is_initially_empty(self):
        bank = Bank()
        self.assertEqual({}, bank.accounts)
        self.assertEqual(len(bank.accounts),0)
    
    def test_add_account(self):
        bank = Bank()

        account_1 = Account("001",50)
        account_2 = Account("002", 100)
        
        bank.add_account(account_1)
        bank.add_account(account_2)
   
        self.assertEqual(len(bank.accounts),2)

    def test_get_account_balance(self):
        bank = Bank()

        account_1 = Account("001", 50)

        bank.add_account(account_1)

        self.assertEqual(bank.get_account_balance("001"), 50)

    def test_withdraw_from_account(self):
        bank = Bank()

        account_2 = Account("002", 100)

        bank.add_account(account_2)

        self.assertEqual(bank.withdraw_from("002", 50), 50)
        
    def test_withdraw_from_method_raises_typeerror_if_not_ints(self):
        bank = Bank()
        
        account_2 = Account("002", 100)
        
        bank.add_account(account_2)

        self.assertRaises(TypeError, bank.withdraw_from, "002", "50")

    def test_account_does_not_exists(self):
        bank = Bank()
        
        self.assertIn(Account("003",20),bank.accounts)

    def test_withdraw_from_method_insufficient_amount(self):
        bank = Bank()

        account_2 = Account("002", 100)

        bank.add_account(account_2)

        #self.assertLess(bank.withdraw_from("002", 120), 0)
        self.assertEqual('Insufficient Funds', bank.withdraw_from("002", 120)) 
  
if __name__ == '__main__':
    unittest.main()


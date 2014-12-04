"""DOCSTRING"""
from flask import Flask, render_template, request
from account import Account
from bank import Bank

APP = Flask(__name__)
BANK = Bank()

@APP.route('/')
def hello_world():
    """Takes the information from the account_number form in index.html"""
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)

if __name__ == '__main__':
    account = Account('1111', 50) #pylint:disable=C0103
    BANK.add_account(account)
    APP.run(debug=True)

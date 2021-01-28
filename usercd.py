class User:
    def __init__(self, name, email):
        self.name =  name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)


jason = User("Jason", "jason@python.com")
agnes = User("Agnes", "agnes@python.com")
deku = User("Deku", "deku@python.com")

jason.make_deposit(1000)
jason.make_deposit(500)
jason.make_deposit(50)
jason.make_withdrawl(200)
jason.display_user_balance()

agnes.make_deposit(2000)
agnes.make_deposit(100)
agnes.make_withdrawl(50)
agnes.make_withdrawl(50)
agnes.display_user_balance()

deku.make_deposit(1000)
deku.make_withdrawl(25)
deku.make_withdrawl(25)
deku.make_withdrawl(25)
deku.display_user_balance()

jason.transfer_money(deku,1000)
jason.display_user_balance()
deku.display_user_balance()


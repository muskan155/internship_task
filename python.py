class Account:
    def __init__(self, name, balance):
        self.name =  name
        self.balance = balance
    def __add__(self, otherobj):
        return self.balance + otherobj.balance

ac1 = Account(name = "Kshitiz", balance = 5845646638565)
ac2 = Account(name = "Kshitiz", balance = 4245575738565 )
ac1 + ac2
print(ac1 + ac2)
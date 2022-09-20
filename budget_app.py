
class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.credit = 0

    def __str__(self):
        header = f" {self.name} ".center(30, "*")
        for item in self.ledger:
            
            description_body = f"\n {item['description']}".ljust(23)
            decimal_number = round(item['amount']*100/100,2)
            amount_body= f"{decimal_number}".rjust(7)

            header= header+description_body+amount_body
        return header

    def update_credit(self):
        self.credit = sum([amount['amount'] for amount in self.ledger])
        pass

    def deposit(self, amount, description=""):

        object = {"amount": amount, "description": description}
        self.ledger.append(object)

    def withdraw(self, amount, description=""):

        self.update_credit()

        if self.credit <= 0:
            return False

        object = {"amount": amount*-1, "description": description}
        self.ledger.append(object)
        
        return True
    
    def get_balance(self):
        return self.credit

    def transfer(self, category, amount):
        self.update_credit()

        if amount <= self.credit:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.credit >= amount:
            return True
        else :
            return False

if __name__ == "__main__":

    x = Category("Food")
    x.deposit(500)

    y = Category("Clothes")
    
    x.transfer(y, 100)

    print(x)
    print('')
    print(y)

    
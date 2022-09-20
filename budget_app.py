
from unicodedata import category


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

def create_spend_chart(category_list):

    total_spent_category = []
    dict_list = []

    for category in category_list:

        total_withdraws = 0

        for item in category.ledger:
            if item['amount'] < 0:
                total_withdraws= total_withdraws + item['amount']
        
        total_spent = {f"{category.name}":f"{total_withdraws}"}
        total_spent_category.append(total_spent)

    # print(total_spent_category)

    percentage_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    chart = "Percentage spent by category" 
    for percent in percentage_list:
        chart = chart+ f"\n{percent}"
    chart = chart+"\n---------"

    # print(chart)

    for item in total_spent_category:
        dict_list.append(*item.items()) ## appending the result inside the list

    print(dict_list)

if __name__ == "__main__":

    x = Category("Food")
    x.deposit(500)

    y = Category("Clothes")
    
    x.transfer(y, 100)

    x.withdraw(200, "Party")

    print(x)
    print('')
    print(y)
    print('')

    create_spend_chart([x, y])
    
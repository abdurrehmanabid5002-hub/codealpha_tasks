stock_price = {"AAPL": 180, "TSLA": 250, "MSFT": 350, "GOOGL": 150}
Total_investment = 0
portfolio=[]
while True:
    stocks = input(("enter the stock to buy :")).upper()
    if stocks.lower() == "exit":
        break
    else:
        quantity = int(input("enter the the quantity to buy stocks: "))
        if stocks in stock_price:
            price = stock_price[stocks]

            Investment = price * quantity
            print(f"{stocks} {quantity} Sharres = {Investment}$")
            Investment_ = f"{stocks} {quantity} Shares = {Investment}$"
            Total_investment += Investment
            print(f"Total_investment of all these shares is {Total_investment}")
            portfolio.append(Investment_)

        else:
            print("Enter the correct stock ")

with open("Task2(Stock Portfolio Tracker/Portfolio.txt", "w") as f:
        for items in portfolio:
             f.write(f"{items}\n")
        f.write(f"\nTotal Investment = {Total_investment}$")
print("File is written succesfully ")



# ''' 
# I also completed this task using Object-Oriented Programming (OOP) with classes and constructors
# '''


'''
class portfolio_tracker:

    def __init__(self):
        self.stock_price = {
            "AAPL": 180,
            "TSLA": 250,
            "MSFT": 350,
            "GOOGL": 150
        }
        self.Total_investment = 0
        self.portfolio = []

    def run(self):
        while True:
            stocks = input("enter the stock to buy :").upper()

            if stocks == "EXIT":
                break

            else:
                quantity = int(input("enter the the quantity to buy stocks: "))

                if stocks in self.stock_price:
                    price = self.stock_price[stocks]

                    Investment = price * quantity

                    print(f"{stocks} {quantity} Sharres = {Investment}$")

                    Investment_ = f"{stocks} {quantity} Shares = {Investment}$"

                    self.Total_investment += Investment

                    print(f"Total_investment of all these shares is {self.Total_investment}")

                    self.portfolio.append(Investment_)

                else:
                    print("Enter the correct stock ")

    def file_save(self):
        with open("Portfolio.txt", "w") as f:
            for items in self.portfolio:
                f.write(f"{items}\n")

            f.write(f"\nTotal Investment = {self.Total_investment}$")

        print("File is written succesfully")


tracker = portfolio_tracker()
tracker.run()
tracker.file_save() 

'''
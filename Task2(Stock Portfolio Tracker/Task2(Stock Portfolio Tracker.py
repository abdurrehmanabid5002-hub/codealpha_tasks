stock_price = {"AAPL": 180, "TSLA": 250, "MSFT": 350, "GOOGL": 150}
Total_investment = 0
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
            Investment1 = f"{stocks} {quantity} Sharres = {Investment}$"
            Total_investment += Investment
            print(Total_investment)

        else:
            print("Enter write stock ")

with open("Portfolio.txt", "w") as f:
    f.write(str(Investment1))
    f.write(f"\nTotal Investment = {Total_investment}$")
print("File is written succesfully ")

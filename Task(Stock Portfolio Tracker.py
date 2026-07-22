stock_price = {"AAPL": 180, "TSLA": 250, "MSFT": 350, "GOOGL": 150}

stocks = input(("enter the stock to buy :"))
quantity =int (input ("enter the the quantity to buy stocks: "))
if stocks in stock_price:
    price = stock_price[stocks]

    Investment = price * quantity
    print ( f"{stocks}:{Investment}")
else:
    print ( "Enter write stock ")
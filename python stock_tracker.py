

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

# Store user investments
portfolio = {}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Take input from user
n = int(input("\nHow many different stocks do you want to buy? "))

for i in range(n):

    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

        investment = stock_prices[stock_name] * quantity

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        total_investment += investment

        print("Investment in", stock_name, "=", "$", investment)

    else:
        print("Stock not available!")

# Display portfolio
print("\n========== YOUR PORTFOLIO ==========")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity

    print(stock, "| Quantity:", quantity, "| Value: $", value)

print("\nTotal Investment Value: $", total_investment)

# Save result in a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | Value: ${value}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved successfully in portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")

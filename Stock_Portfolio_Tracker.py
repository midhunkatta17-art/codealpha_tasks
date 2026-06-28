# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

total_investment = 0

print("===================================")
print("    STOCK PORTFOLIO TRACKER")
print("===================================")

num_stocks = int(input("Enter the number of different stocks: "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Price per share:", stock_prices[stock_name])
        print("Investment:", investment)
    else:
        print("Stock not found!")

print("\n===================================")
print("Total Investment Value =", total_investment)
print("===================================")

# Optional: Save result to a text file
choice = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if choice == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment Value = " + str(total_investment))
    file.close()
    print("Result saved successfully in portfolio.txt")
else:
    print("Result not saved.")

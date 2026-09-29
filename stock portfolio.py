# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

print("Stock Portfolio Tracker")
print("-----------------------")

# Display available stocks
print("Available stocks:", ", ".join(stock_prices.keys()))

# Ask the user for stock name
stock = input("Enter stock name: ").upper()

# Check if stock exists
if stock in stock_prices:

    # Ask for quantity
    quantity = int(input("Enter quantity: "))

    # Calculate total investment
    total_value = stock_prices[stock] * quantity

    print("\nStock:", stock)
    print("Price per share: $", stock_prices[stock])
    print("Quantity:", quantity)
    print("Total investment: $", total_value)

else:
    print("Sorry, that stock is not available.")
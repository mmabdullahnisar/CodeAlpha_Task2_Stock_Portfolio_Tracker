stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00
}

portfolio = {}

print("Stock Portfolio Tracker")
print("Available stocks and prices:")

for stock, price in stock_prices.items():
    print(stock, "-", "$" + format(price, ".2f"))

while True:
    stock_name = input("\nEnter stock symbol or type done: ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("This stock is not available.")
        continue

    try:
        quantity = float(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid quantity.")
        continue

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

if not portfolio:
    print("\nNo stocks were added.")
else:
    total_investment = 0
    report_lines = ["Stock Portfolio Summary", ""]

    print("\nPortfolio Summary")

    for stock_name, quantity in portfolio.items():
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        line = stock_name + " | Quantity: " + format(quantity, ".2f") + " | Value: $" + format(investment, ".2f")
        print(line)
        report_lines.append(line)

    total_line = "Total Investment: $" + format(total_investment, ".2f")
    print(total_line)
    report_lines.append("")
    report_lines.append(total_line)

    save_choice = input("\nSave the result to a text file? yes/no: ").lower().strip()

    if save_choice == "yes" or save_choice == "y":
        with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(report_lines))

        print("Portfolio saved in portfolio_summary.txt")

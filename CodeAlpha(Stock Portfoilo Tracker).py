stocks = {
    "aapl": 180,
    "tsla": 250,
    "samsung": 170,
    "toyota": 200,
    "google": 150,
    "coca_cola": 300,
    "flipkart": 210,
    "fortuner": 50,
    "dell": 105,
    "amazon": 150
}

total_investment = 0

n = int(input("How many different stocks do you want to enter number ? "))

for i in range(n):

    stock_name = input(f"Enter stock {i+1} name: ").lower()
    quantity = int(input(f"Enter quantity of {stock_name}: "))

    if stock_name in stocks:

        stock_value = stocks[stock_name] * quantity
        total_investment += stock_value

        print(f"Value of {stock_name} = {stock_value}")

    else:
        print(f"{stock_name} is not found in our database.")

print(f"\nTotal Investment Value = {total_investment}")
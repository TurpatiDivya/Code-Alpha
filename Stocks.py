import requests

# Alpha Vantage API key
API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'

def get_stock_data(symbol):
    """Fetch stock data from Alpha Vantage"""
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def add_stock(portfolio, symbol, shares):
    """Add a stock to the portfolio"""
    if symbol in portfolio:
        portfolio[symbol]['shares'] += shares
    else:
        data = get_stock_data(symbol)
        if 'Global Quote' in data:
            price = float(data['Global Quote']['05. price'])
            portfolio[symbol] = {'shares': shares, 'price': price}

def remove_stock(portfolio, symbol, shares):
    """Remove shares from a stock in the portfolio"""
    if symbol in portfolio:
        if portfolio[symbol]['shares'] >= shares:
            portfolio[symbol]['shares'] -= shares
        else:
            print(f"Not enough shares of {symbol} in the portfolio.")
    else:
        print(f"{symbol} is not in the portfolio.")

def portfolio_value(portfolio):
    """Calculate the total value of the portfolio"""
    total_value = 0
    for symbol, data in portfolio.items():
        total_value += data['shares'] * data['price']
    return total_value

def main():
    portfolio = {}
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Value")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(portfolio, symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            remove_stock(portfolio, symbol, shares)
        elif choice == '3':
            print(f"Total Portfolio Value: ${portfolio_value(portfolio):.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()

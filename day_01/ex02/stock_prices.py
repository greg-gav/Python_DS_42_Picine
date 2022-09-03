import sys

def run():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) != 2:
        sys.exit(1)
    if sys.argv[1].capitalize() not in COMPANIES.keys():
        print("Unknown company")
        sys.exit(1)
    print(STOCKS[COMPANIES[sys.argv[1].capitalize()]])

if __name__ == "__main__":
    run()
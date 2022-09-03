import sys


def run():
    COMPANIES = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Tesla": "TSLA",
        "Nokia": "NOK",
    }
    STOCKS = {
        "AAPL": 287.73,
        "MSFT": 173.79,
        "NFLX": 416.90,
        "TSLA": 724.88,
        "NOK": 3.37,
    }
    if len(sys.argv) != 2:
        sys.exit(1)
    if sys.argv[1].upper() not in COMPANIES.values():
        print("Unknown ticker")
        sys.exit(1)
    key = list(COMPANIES.keys())[list(COMPANIES.values()).index(sys.argv[1].upper())]
    print(key, STOCKS[sys.argv[1].upper()])


if __name__ == "__main__":
    run()

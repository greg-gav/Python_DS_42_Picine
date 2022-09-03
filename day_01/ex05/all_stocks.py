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
    args = sys.argv[1].split(",")
    for i, arg in enumerate(args):
        args[i] = arg.strip()
        if args[i] == "":
            print()
            sys.exit(1)
    for arg in args:
        if arg.capitalize() in COMPANIES.keys():
            print(
                f"{arg.capitalize()} stock price is {STOCKS[COMPANIES[arg.capitalize()]]}"
            )
        elif arg.upper() in COMPANIES.values():
            key = list(COMPANIES.keys())[list(COMPANIES.values()).index(arg.upper())]
            print(f"{arg.upper()} is a ticker symbol for {key}")
        else:
            print(f"{arg} is an unknown company or an unknown ticker symbol")


if __name__ == "__main__":
    run()

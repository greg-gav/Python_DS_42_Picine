import sys
import time

import requests
from bs4 import BeautifulSoup


class ArgError(Exception):
    pass


def run():
    if len(sys.argv) != 3:
        sys.exit(1)
    ticker = sys.argv[1].lower()
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    re = requests.get(url, headers=headers)
    re.raise_for_status()
    if "lookup" in re.url:
        raise ArgError("Ticker not found")
    soup = BeautifulSoup(re.content, "html.parser")
    div = soup.find("div", {"id": "Main"})
    divs = div.findAll("span")
    lst = [sys.argv[2]]
    for i, span in enumerate(divs):
        if sys.argv[2] in span:
            for j in range(5):
                lst.append(divs[i + j + 1].text)
    if len(lst) == 1:
        raise ArgError(f"Field not found {sys.argv[2]}")
    print(tuple(lst))
    return tuple(lst)


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"Caught error: {e}")
        sys.exit(1)

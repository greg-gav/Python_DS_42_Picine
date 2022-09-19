#!python3

import os

def run():
    print(f"Your current virtual env is {os.environ['VIRTUAL_ENV']}")

if __name__ == "__main__":
    try:
        run()
    except KeyError as e:
        print(f"KeyError exception {e}")
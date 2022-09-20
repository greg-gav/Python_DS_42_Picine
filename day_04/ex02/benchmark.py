#!python3
import sys
from timeit import Timer


def comp(emails):
    lst = [x for x in emails if x.endswith("@gmail.com")]

def loop(emails):
    lst = []
    for email in emails:
        if email.endswith("@gmail.com"):
            lst.append(email)

def maps(emails):
    lst = []
    [*map(lambda x: lst.append(x) if x.endswith("@gmail.com") else True, emails)]

def filters(emails):
    lst = list(filter(lambda x: x.endswith("@gmail.com"), emails))

def run():
    if len(sys.argv) != 3:
        sys.exit(1)
    if sys.argv[1] not in ('loop', 'list_comprehension', 'map', 'filter'):
        sys.exit(1)
    num = int(sys.argv[2])
    emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
    ]
    
    if sys.argv[1] == "loop":
        func = Timer(lambda: loop(emails))
        result = func.timeit(number=num)
    if sys.argv[1] == "list_comprehension":
        func = Timer(lambda: comp(emails))
        result = func.timeit(number=num)
    if sys.argv[1] == "map":
        func = Timer(lambda: maps(emails))
        result = func.timeit(number=num)
    if sys.argv[1] == "filter":
        func = Timer(lambda: filters(emails))
        result = func.timeit(number=num)
    print(result)

    
if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"Error caught: {e}")
#!python3
from timeit import Timer

def comp(emails):
    lst = [x for x in emails]

def loop(emails):
    lst = []
    for email in emails:
        lst.append(email)

def maps(emails):
    lst = list(map(str, emails))


def run():
    emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
    ]
    num = 900000
    loop_t = Timer(lambda: loop(emails))
    comp_t = Timer(lambda: comp(emails))
    comp_m = Timer(lambda: maps(emails))
    print("Running comparison... please wait")
    maps(emails)
    times = {
        loop_t.timeit(number=num) : "it is better to use a loop",
        comp_t.timeit(number=num) : "it is better to use a list comprehension",
        comp_m.timeit(number=num) : "it is better to use a map",
    }
    ordered = sorted(times)
    print(times[ordered[0]])
    print(f"{ordered[0]} vs {ordered[1]} vs {ordered[2]}")

if __name__ == "__main__":
    run()
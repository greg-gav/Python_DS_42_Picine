#!python3
from timeit import Timer

def comp(emails):
    lst = [x for x in emails if x.endswith("@gmail.com")]

def loop(emails):
    lst = []
    for email in emails:
        if email.endswith("@gmail.com"):
            lst.append(email)

def run():
    emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
    ]
    num = 90000000
    loop_t = Timer(lambda: loop(emails))
    comp_t = Timer(lambda: comp(emails))
    times = [loop_t.timeit(number=num), comp_t.timeit(number=num)]
    if times[0] < times[1]:
        print ("it is better to use a loop")
    else:
        print("it is better to use a list comprehension")
    print(f"{sorted(times)[0]} vs {sorted(times)[1]}")

if __name__ == "__main__":
    run()
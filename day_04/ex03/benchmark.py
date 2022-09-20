#!python3
import sys
from timeit import Timer
from functools import reduce


def sum_loop(up_to):
    sum = 0
    for i in range(1, up_to + 1):
        sum += i * i

def sum_reduce(up_to):
    sum = reduce(lambda x, y: x + y * y, range(1, up_to + 1))


def run():
    if len(sys.argv) != 4:
        sys.exit(1)
    if sys.argv[1] not in ("loop", "reduce"):
        sys.exit(1)
    count = int(sys.argv[2])
    number = int(sys.argv[3])

    if sys.argv[1] == "loop":
        func = Timer(lambda: sum_loop(number))
        result = func.timeit(number=count)
    if sys.argv[1] == "reduce":
        func = Timer(lambda: sum_reduce(number))
        result = func.timeit(number=count)
    print(result)


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"Error caught: {e}")

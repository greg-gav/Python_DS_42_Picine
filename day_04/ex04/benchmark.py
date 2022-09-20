#!python3
import random

from timeit import Timer
from collections import Counter


def get_dict_my(numbers):
    book = {}
    for num in numbers:
        if num in book.keys():
            book[num] += 1
        else:
            book[num] = 1

def get_my_top(numbers):
    book = {}
    for num in numbers:
        if num in book.keys():
            book[num] += 1
        else:
            book[num] = 1
    sort = sorted(book.values(), reverse=True)
    top_book = {}
    for i in range(10):
        top_book[list(book.keys())[list(book.values()).index(sort[i])]] = sort[i]

def dict_counter(numbers):
    cnt = Counter()
    for num in numbers:
        cnt[num] += 1
    dict(cnt)

def top_counter(numbers):
    dict(Counter(numbers).most_common(10))

def run():
    numbers = [random.randint(0, 100) for _ in range(1000000)]
    func = Timer(lambda: get_dict_my(numbers))
    result = func.timeit(number=1)
    print(f"my function: {result}")
    func = Timer(lambda: dict_counter(numbers))
    result = func.timeit(number=1)
    print(f"Counter: {result}")
    func = Timer(lambda: get_my_top(numbers))
    result = func.timeit(number=1)
    print(f"my top: {result}")
    func = Timer(lambda: top_counter(numbers))
    result = func.timeit(number=1)
    print(f"Counter's top: {result}")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"Error caught: {e}")

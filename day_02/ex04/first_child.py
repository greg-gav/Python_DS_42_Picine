import sys
from random import randint


class Research:
    def __init__(self, path):
        self._path = path

    def file_reader(self, has_header=True):
        expected_data = ("0", "1")
        try:
            with open(f"{self._path}", "r") as file:
                lines = file.readlines()
                if has_header:
                    h1, h2 = lines[0].split(",")
                result = []
                for line in lines[1:] if has_header else lines:
                    v1, v2 = line.split(",")
                    if (
                        v1.strip() not in expected_data
                        or v2.strip() not in expected_data
                    ):
                        raise ValueError(f"Unexpected data")
                    if v1.strip() == v2.strip():
                        raise ValueError(f"Unexpected data")
                    result.append([int(x.strip()) for x in line.split(",")])
                self._data = result
                return result
        except Exception as e:
            print(f"Error caught: {e}")
            sys.exit(1)

    class Calculations:
        def __init__(self, data):
            self._data = data

        def counts(self):
            heads, tails = 0, 0
            for toss in self._data:
                if toss[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        def fractions(self, heads, tails):
            head_f = heads / (heads + tails) * 100
            tails_f = tails / (heads + tails) * 100
            return head_f, tails_f

    class Analytics(Calculations):
        def predict_random(self, tosses):
            returned = []
            for _ in range(tosses):
                toss = randint(0, 1)
                if toss == 1:
                    returned.append([1, 0])
                elif toss == 0:
                    returned.append([0, 1])
            return returned

        def predict_last(self):
            return self._data[len(self._data) - 1]


def run():
    if len(sys.argv) != 2:
        sys.exit(1)
    research = Research(sys.argv[1])
    data = research.file_reader()
    calculations = Research.Calculations(data)
    analytics = Research.Analytics(data)
    heads, tails = calculations.counts()
    heads_f, tails_f = calculations.fractions(heads, tails)
    predict = analytics.predict_random(3)
    last = analytics.predict_last()
    print(data)
    print(f"{heads}, {tails}")
    print(f"{heads_f}, {tails_f}")
    print(predict)
    print(last)


if __name__ == "__main__":
    run()

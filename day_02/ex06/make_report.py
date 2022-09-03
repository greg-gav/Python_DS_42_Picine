import sys

from analytics import Research
from config import num_of_steps


def make_report():
    if len(sys.argv) != 2:
        sys.exit(1)
    research = Research(sys.argv[1])
    data = research.file_reader()
    analytics = Research.Analytics(data)
    predict = Research.Analytics(analytics.predict_random(num_of_steps))
    analytics.save_file(predict, 'report', 'txt')


if __name__ == "__main__":
    make_report()

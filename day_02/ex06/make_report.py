import sys

from analytics import Research
from config import num_of_steps


def make_report():
    if len(sys.argv) != 2:
        sys.exit(1)
    research = Research(sys.argv[1])
    try:
        data = research.file_reader()
        analytics = Research.Analytics(data)
        predict = Research.Analytics(analytics.predict_random(num_of_steps))
        analytics.save_file(predict, 'report', 'txt')
        research.slack_send("The report has been successfully created")
    except Exception:
        research.slack_send("The report hasn’t been created due to an error")



if __name__ == "__main__":
    try:
        make_report()
    except Exception as e:
        print(f"Exception caught: {e}")

import sys


def run():
    if len(sys.argv) != 2:
        exit(1)

    with open("employees.tsv", "r") as file:
        people = file.readlines()
    for person in people:
        info = [x.strip() for x in person.split("\t")]
        if sys.argv[1] in info:
            print(
                f"Dear {info[0]}, welcome to our team. "
                f"We are sure that it will be a pleasure to work with you. "
                f"That’s a precondition for the professionals that our company hires."
            )


if __name__ == "__main__":
    run()

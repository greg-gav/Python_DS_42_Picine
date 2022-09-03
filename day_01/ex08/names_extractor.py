import sys


def run():
    if len(sys.argv) != 2:
        exit(1)
    with open(sys.argv[1], 'r') as file:
        emails = file.readlines()
    with open('employees.tsv', 'w') as outfile:
        outfile.write("Name\tSurname\tE-mail\n")
        for person in emails:
            outfile.write(f"{person[:person.find('.')].capitalize()}\t")
            outfile.write(f"{person[person.find('.') + 1:person.find('@')].capitalize()}\t")
            outfile.write(f"{person}")


if __name__ == "__main__":
    run()

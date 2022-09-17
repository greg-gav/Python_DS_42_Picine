import sys


def call_center(clients, recipients, participants=None):
    to_call = set(clients)  - set(recipients)
    print(list(to_call))


def potential_clients(clients, participants, recipients=None):
    not_clients = set(participants) - set(clients)
    print(list(not_clients))


def loyalty_program(clients, participants, recipients=None):
    loyalty = set(clients) - set(participants)
    print(list(loyalty))


def run():
    clients = [
        "andrew@gmail.com",
        "jessica@gmail.com",
        "ted@mosby.com",
        "john@snow.is",
        "bill_gates@live.com",
        "mark@facebook.com",
        "elon@paypal.com",
        "jessica@gmail.com",
    ]
    participants = [
        "walter@heisenberg.com",
        "vasily@mail.ru",
        "pinkman@yo.org",
        "jessica@gmail.com",
        "elon@paypal.com",
        "pinkman@yo.org",
        "mr@robot.gov",
        "eleven@yahoo.com",
    ]
    recipients = [
        "andrew@gmail.com",
        "jessica@gmail.com",
        "john@snow.is"
    ]
    if len(sys.argv) != 2:
        exit(1)
    globals()[f"{sys.argv[1]}"](
        clients=clients,
        participants=participants,
        recipients=recipients
    )


if __name__ == "__main__":
    run()

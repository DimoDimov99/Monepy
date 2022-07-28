import os

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

COMMANDS = {
    "log expense": "logging a new expense for the month",
    "expenses check": "provide you expenses with certain category for month & year",
    "list spendings": "List all spendings for current month",
    "list total month spendings": "List total amount of money spend for month",
    "save": "Save currnet total spend expenses value for the month",
    "quit": "quits the application"
}

EXPENSES_TAGS = {
    "1": "FOOD",
    "2": "FUEL",
    "3": "RELAX",
    "4": "EDUCATION",
    "5": "COSMETIC",
    "6": "OUTSIDE EATING",
    "7": "OTHER"
}

def clear():
    os.system("clear")


def display_commands():
    for name, command in COMMANDS.items():
        print(f"{name} -> {command}".strip("\n"))
        print(30 * "-")


def display_expenses_tags():
    print("ALL AVAILABLE EXPENSE TAGS:")
    for name, command in EXPENSES_TAGS.items():
        print(f"{name} -> {command}".strip("\n"))
        print(30 * "-")

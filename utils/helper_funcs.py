import os
import platform
from datetime import datetime

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
    "7": "OUTSIDE RELAX",
    "8": "SUPPLEMENTS",
    "9": "PRESENTS",
    "10": "OTHER"
}


def clear():
    current_os = platform.system()
    if current_os == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def display_commands():
    for name, command in COMMANDS.items():
        print(f"{name} -> {command}".strip("\n"))
        print(30 * "-")


def display_expenses_tags():
    print("ALL AVAILABLE EXPENSE TAGS:")
    for name, command in EXPENSES_TAGS.items():
        print(f"{name} -> {command}".strip("\n"))
        print(30 * "-")


def get_month():
    return datetime.now().strftime("%B")


def get_current_month_day():
    return datetime.now().strftime("%d")

def get_current_year():
    return datetime.now().strftime("%Y")


def get_root_dir():
    return os.getcwd()
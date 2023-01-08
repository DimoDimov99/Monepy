import os
import platform
from datetime import datetime


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


COMMANDS = {
    "log expense": "logging a new expense for the month",
    "expenses check": "provide you with information regarding the expenses from certain category for month & year",
    "list spendings": "List all spendings for current month",
    "reset": "reset to custom value, the last saved value from expense in 'value.txt' file",
    "save all categories spendings": "Save into 'total_spendings_report.txt' file all spending by categories for the current month and the total amount",
    "display category spendings": "Display all spendings by categories for the current month and the total amount",
    "print user spendings for month": "Prints user spendings (Dimo, Radina or Both) for currently provided month",
    "total spendings for month and saved money": "Prints total spendings for month, earned salary and potentialy saved money for the given month",
    "quit": "quits the application"
}

EXPENSES_TAGS = {
    "1": "FOOD",
    "2": "CAR",
    "3": "RELAX",
    "4": "EDUCATION",
    "5": "COSMETIC",
    "6": "OUTSIDE EATING",
    "7": "HAVE FUN",
    "8": "SUPPLEMENTS",
    "9": "PRESENTS",
    "10": "CHARITY",
    "11": "TECHNOLOGY",
    "12": "OTHER",
}

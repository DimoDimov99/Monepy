from datetime import datetime
from importlib.abc import FileLoader
import os
import time
import re
from utils.helper_funcs import EXPENSES_TAGS, clear, display_expenses_tags, get_month, get_current_month_day, get_current_year, get_root_dir


ROOT_DIR = get_root_dir()


def check_if_in_ROOT_DIR():
    if os.getcwd() != ROOT_DIR:
        os.chdir(ROOT_DIR)


def reset_total_money_spend_value():
    with open("value.txt", "w", encoding="utf8") as file:
            file.write("0")


def check_str_for_number(str_input):
    re_numbers = re.compile('\d')
    return False if (re_numbers.search(str_input) == None) else True


def get_all_expenses_tags():
    expenses_tags = []

    for tag in EXPENSES_TAGS.values():
        expenses_tags.append(tag)

    return expenses_tags


def sum_expenses_values(arr):
    total = 0
    for i in arr:
        total += i
    total = "{:.2f}".format(total)
    return total


def clear_file_content(filename):
    with open(filename, "w", encoding="utf8"):
        pass



def reset_last_money_value_spend():
    value_filename = "value.txt"
    clear()
    check_if_in_ROOT_DIR()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    clear()
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1

    FLAG = is_value_file_exist()
    if FLAG:
        print(f"'{value_filename}' file exist!")
        user_input = input("Do you want to reset the value to 0?: ")
        if user_input.lower() == "y":
            with open(value_filename, "w", encoding="utf8") as file:
                file.write("0")
        elif user_input.lower() == "n":
            print(f"{value_filename} file is not reseted!")
        else:
            print("Invalid input!")
            return -1
    elif not FLAG:
        print(f"{value_filename} file does not exist!")
        return -1


def create_work_dir():
    current_month = get_month()
    current_location = os.getcwd()
    current_year = get_current_year()
    if current_location != ROOT_DIR:
        os.chdir(ROOT_DIR)

    destination_path = f"{current_location}/{current_month}_{current_year}"
    if current_month and current_year and os.path.exists(destination_path):
        os.chdir(destination_path)
        # print(os.getcwd())
    else:
        # print(f"{current_month} directory is missing! Creating it now")
        os.makedirs(destination_path)
        time.sleep(1)
        os.chdir(destination_path)


def return_work_directory_txt_files() -> None:
    """Function to return all txt files inside the current directory"""
    txt_files = []
    for x in os.listdir():
        if x.endswith(".txt"):
            txt_files.append(x)
    return txt_files



def is_value_file_exist():
    file_exist_flag = False
    all_txt_files = return_work_directory_txt_files()
    if "value.txt" in all_txt_files:
        file_exist_flag = True
    return file_exist_flag


def list_all_dirs() -> None:
    """Function to display all directories inside the current directory"""
    folder = os.getcwd()
    # subfolders = [f.name for f in os.scandir(folder) if f.is_dir() and f.name in MONTHS] # deprecated most likely will be deleted!
    subfolders = [f.name for f in os.scandir(folder) if f.is_dir() and f.name[0].isupper()] # "f.name[0].isupper() checp and diry fix, works for now :D"
    # main point of "f.name[0].isupper()" is to display only folders with Capitalized letter, which means it will display only Months folders and ignore oders!
    print("All directories: ")
    for folders in subfolders:
        print(folders)


def list_spendings() -> None:
    clear()
    check_if_in_ROOT_DIR()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    clear()
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    txt_input = f"{custom_dir}_finance_report.txt"
    try:
        clear()
        with open(txt_input, "rt", encoding="utf8") as task_file:
            lines = task_file.readlines()
            if len(lines) == 0:
                print("The file is empty")
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"Looks like the file {txt_input} does not exist!")


def write_expense_report():
    check_if_in_ROOT_DIR()
    total_money_spend = 0
    current_month = get_month()
    # current_year = get_current_year()
    create_work_dir()
    display_expenses_tags()
    stuff_tag = input("Enter a category tag: ")
    try:
        stuff_tag = EXPENSES_TAGS[stuff_tag]
    except KeyError:
        print("Invalid Expenses tag!")
        return -1

    stuff_name = input("Enter a thing you spend money on: ")

    if check_str_for_number(stuff_name):
        print("The activity you spend money on cannot contain digits!")
        return -1

    try:
        stuff_price = float(input("Enter the price you spend: "))
    except ValueError:
        print("Invalid value!")
        return -1

    text_file_name = f"{current_month}_{get_current_year()}_finance_report.txt"


    if not os.path.exists("value.txt"):
        reset_total_money_spend_value()

    with open("value.txt", "rt", encoding="utf8") as file:
        value = file.readline().strip("\n")
        value = float(value)
        total_money_spend = value + stuff_price

    with open("value.txt", "w", encoding="utf8") as file:
        file.write(f"{total_money_spend}")


    with open(text_file_name, "a", encoding="utf8") as file:
        stuff_price = "{:.2f}".format(stuff_price)
        total_money_spend = "{:.2f}".format(total_money_spend)
        file.write(f"[{stuff_tag} {get_current_year()}] You spend: [{stuff_price} lv] for [{stuff_name}] on [{datetime.now().strftime('%B %d %Y')}] at [{datetime.now().strftime('%H:%M:%S')}]\n")
        file.write(f"[{stuff_tag} {get_current_year()}] Total spending for the month: [{total_money_spend} lv]")
        file.write("\n")
        file.write("--------------------------------------\n")


def output_total_sum_for_expenses_tag(filename):
    result = []
    total_sum = 0
    step = 2
    first_num_index = 1
    second_num_index = 2


    with open(filename, "rt", encoding="utf8") as file:
        for lineno, line in enumerate(file):
            if lineno % step == 0:
                #print(line.strip("\n"))
                for digit in re.findall(r'\d+', line):
                    result.append(digit)


    while first_num_index < len(result) and second_num_index < len(result):
        join_to_digits = f"{result[first_num_index]}.{result[second_num_index]}"
        result_to_numeric = float(join_to_digits)
        total_sum += result_to_numeric
        first_num_index += 8
        second_num_index += 8
                #for digit in re.findall(r'\d+', content):
                #result.append(digit)

    formatted_output = format(total_sum, '.2f')
    return formatted_output



def print_category_spendings():
    TEMPT_FILENAME = "tempt.txt"
    default_path = os.getcwd()
    if default_path != ROOT_DIR:
        os.chdir(ROOT_DIR)
    clear()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.capitalize()
    custom_dir_stripped = custom_dir.rpartition("_")
    custom_dir_month = custom_dir_stripped[0]
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    clear()
    display_expenses_tags()
    check_category_keyword = input("For which category you want you to check: ")

    try:
        check_category_keyword = EXPENSES_TAGS[check_category_keyword]
    except KeyError:
        print("Invalid Expenses tag!")
        return -1

    check_category_year = input("For which year you want to check: ")
    phrase = f"[{check_category_keyword} {check_category_year}]"
    filename = f"{custom_dir}_finance_report.txt"
    EXPENSES_TAGS_DATA = []

    if os.path.isfile(f"{filename}"):
        """Print the lines in the file that contains the given phrase."""
        clear()
        with open(filename, "r") as file:
            for line in file:
                if phrase in line:
                    EXPENSES_TAGS_DATA.append((line.replace("\n", "")))
                    # print(line)
                    # info.append(line)
                    #print(100 * "-")

        with open(f"{TEMPT_FILENAME}", "w", encoding="utf8") as file:
            for i in range(len(EXPENSES_TAGS_DATA)):
                file.write(f"{EXPENSES_TAGS_DATA[i]}\n")

    total_sum_for_expenses_tag = output_total_sum_for_expenses_tag(f"{TEMPT_FILENAME}")

    print(f"You have spend {total_sum_for_expenses_tag} for [{check_category_keyword}] EXPENSES in: {custom_dir_month} {get_current_year()}")

    os.remove(TEMPT_FILENAME)


def save_every_category_total_spending_for_month():
    report_file_name = "total_spendings_report.txt"
    expenses_spendings_values = []
    ALL_AVAILABLE_EXPENSES_TAGS = get_all_expenses_tags()
    TEMPT_FILENAME = "tempt.txt"
    default_path = os.getcwd()
    if default_path != ROOT_DIR:
        os.chdir(ROOT_DIR)
    clear()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.capitalize()
    custom_dir_stripped = custom_dir.rpartition("_")
    custom_dir_month = custom_dir_stripped[0]
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    clear()
    # display_expenses_tags()
    check_category_year = input("For which year you want to check: ")
    clear_file_content(f"{report_file_name}")
    for expense_tag in ALL_AVAILABLE_EXPENSES_TAGS:
        phrase = f"[{expense_tag} {check_category_year}]"
        filename = f"{custom_dir}_finance_report.txt"
        EXPENSES_TAGS_DATA = []
        if os.path.isfile(f"{filename}"):
            clear()
            with open(filename, "r") as file:
                for line in file:
                    if phrase in line:
                        EXPENSES_TAGS_DATA.append((line.replace("\n", "")))
                    # print(line)
                    # info.append(line)
                    #print(100 * "-")
            with open(f"{TEMPT_FILENAME}", "w", encoding="utf8") as file:
                for i in range(len(EXPENSES_TAGS_DATA)):
                    file.write(f"{EXPENSES_TAGS_DATA[i]}\n")
            total_sum_for_expenses_tag = output_total_sum_for_expenses_tag(f"{TEMPT_FILENAME}")
            expenses_spendings_values.append(float(total_sum_for_expenses_tag))

            with open(f"{report_file_name}", "a", encoding="utf8") as file:
                file.write(f"You have spend {total_sum_for_expenses_tag} for {expense_tag}")
                file.write("\n")
                file.write("--------------------------------------\n")

    with open(f"{report_file_name}", "a", encoding="utf8") as file:
        file.write(f"The total amount of all spendings is: {sum_expenses_values(expenses_spendings_values)} lv for {custom_dir_month} {check_category_year}")

    print("Information saved successfully!")
    os.remove(TEMPT_FILENAME)


def list_all_category_spending_for_month() -> None:
    clear()
    check_if_in_ROOT_DIR()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    clear()
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    txt_input = f"total_spendings_report.txt"
    try:
        clear()
        with open(txt_input, "rt", encoding="utf8") as task_file:
            lines = task_file.readlines()
            if len(lines) == 0:
                print("The file is empty")
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"Looks like the file {txt_input} does not exist!")

from utils.report import write_expense_report, print_category_spendings, save_spend_money_for_month, list_spendings, list_total_spendings_for_months, reset_last_money_value_spend
from utils.helper_funcs import clear, display_commands


def main(user_input):
    if user_input == "log expense":
        write_expense_report()
    elif user_input == "expenses check":
        print_category_spendings()
    elif user_input == "list spendings":
        list_spendings()
    elif user_input == "list total month spendings":
        list_total_spendings_for_months()
    elif user_input == "save":
        save_spend_money_for_month()
    elif user_input == "reset":
        reset_last_money_value_spend()
    elif user_input == "commands":
        display_commands()
    else:
        print("Invalid command")


if __name__ == "__main__":
    clear()
    user_input = input("Choose a command to begin: ").lower()
    while user_input != "quit":
        clear()
        main(user_input)
        user_input = input("Choose a command to begin: ").lower()
    print("Quiting")

from expenses_logic.report import write_expense_report, print_category_spendings, list_spendings,\
reset_last_money_value_spend, save_every_category_total_spending_for_month, list_all_category_spending_for_month, print_user_spendings
from utilities.helper_funcs import clear, display_commands


def main(user_input):
    if user_input == "log expense":
        write_expense_report()
    elif user_input == "expenses check":
        print_category_spendings()
    elif user_input == "list spendings":
        list_spendings()
    elif user_input == "reset":
        reset_last_money_value_spend()
    elif user_input == "save all categories spendings":
        save_every_category_total_spending_for_month()
    elif user_input == "display category spendings":
        list_all_category_spending_for_month()
    elif user_input == "print user spendings for month":
        print_user_spendings()
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

import csv
import os.path


def main():
    open_program()
    next_up()

def open_program():
#This function will check whether a CSV file already exists. If it does, the program will know that initial setup has already been completed. If it does not, tbe program will proceed to initial setup.#
    if os.path.isfile('allowance.csv'):
        parent_or_child = input("Are you the parent or child? Type P or C: ")
        if parent_or_child == "p":
            current_balance = parent_maintenance()
        else:
            child_maintenance()
    else:
        name, password, current_balance = initial_setup()

def initial_setup():
    #This function will be initiated upon first use of the app only. It will provide the child's name, a starting balance, and a password for the parent to use when making deposits or deductions from the account#
    name = input("What is your child's first name?: ")
    password = (input("Enter a password: "))
    current_balance = int(input("How much money do you want your child's account to start with?: "))
    with open('allowance.csv', 'w', newline='') as allowance_file:
        writer = csv.writer(allowance_file)
        writer.writerow(['Name', 'Amount'])
        writer.writerow([name, current_balance])
    return name, password, current_balance

def parent_maintenance(current_balance, password):
    #This function will be initiated when a parent uses the app and initial setup has already been completed#
    parent_input = input("Enter password: ")
    if parent_input == password:
        parent_question = input("Do you want to add or deduct money from the account? Type A or D: ")
        if parent_question == "a":
            add_amount = int(input("How much money do you want to add?: "))
            current_balance = (add_amount + current_balance)
            print(current_balance)
            return current_balance
    else:
        parent_input = input("Incorrect password. Please try again: ")
        if parent_input == password:
            parent_question = input("Do you want to add or deduct money from the account? Type A or D: ")
            if parent_question == "a":
                add_amount = int(input("How much money do you want to add?: "))
                current_balance = (add_amount + current_balance)
                print(current_balance)
                return current_balance
        else:
            print("Incorrect password. Exiting app")
            open_program()


def next_up(current_balance):
    #This function will be initiated after initial setup of the program#
    choice = input("What would you like to do now? You can add money (a), deduct money (d), view balance (v), or exit parental section (e). Enter choice:  ")
    if choice == "a":
        add_amount = int(input("How much money do you want to add?: "))
        current_balance = (add_amount + current_balance)
        print("$" + current_balance)
    elif choice == "d":
        deduct_amount = int(input("How much money do you want to deduct?: "))
        current_balance = (current_balance - deduct_amount)
        print("$" + current_balance)
    elif choice == "v":
        print("$" + current_balance)
    elif choice == "e":
        open_program()
    return current_balance

if __name__ == '__main__':
    main()
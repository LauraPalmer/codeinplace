import csv
import os.path


def main():
    open_program()

def open_program():
#This function will check whether a CSV file already exists. If it does, the program will know that initial setup has already been completed. If it does not, tbe program will proceed to initial setup.#
    if os.path.isfile('allowance.csv'):
        parent_or_child = input("Are you the parent or child? Type P or C")
        if parent_or_child == "p":
            current_balance = parent_maintenance()
        else:
            child_maintenance()
    else:
        name, current_balance = initial_setup()

def initial_setup():
    #This function will be initiated upon first use of the app only. It will provide the child's name, a starting balance, and a password for the parent to use when making deposits or deductions from the account#
    name = input("What is your child's first name?: ")
    current_balance = int(input("How much money do you want your child's account to start with?: "))
    with open('allowance.csv', 'w', newline='') as allowance_file:
        writer = csv.writer(allowance_file)
        writer.writerow(['Name', 'Amount'])
        writer.writerow([name, current_balance])
    return name, current_balance

def parent_maintenance(current_balance):
    #This function will be initiated when a parent uses the app and initial setup has already been completed#
    parent_input = input("Enter password: ")
    if parent_input == parent_password:
        parent_question = input("Do you want to add or deduct money from the account? Type A or D: ")
        if parent_question == a:
            add_amount = input(int("How much money do you want to add? "))
            current_balance = (add_amount + current_balance)
            print(current_balance)
            return current_balance




if __name__ == '__main__':
    main()
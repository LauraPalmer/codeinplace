import csv
import os.path

def main():
    open_program()

def open_program():
#This function will check whether a CSV file already exists. If it does, the program will know that initial setup has already been completed. If it does not, tbe program will proceed to initial setup.#
    if os.path.isfile('allowance.csv'):
        child_name, current_balance = open_csv('allowance.csv')
        print(child_name, current_balance)
        parent_or_child = input("Are you the parent or child? Type P or C: ")
        if parent_or_child == "p" or parent_or_child == "P":
            current_balance = parent_maintenance(child_name, current_balance)
        else:
            child_maintenance(child_name, current_balance)
        open_program()
    else:
        child_name, current_balance = initial_setup()
    return child_name, current_balance

def initial_setup():
    #This function will be initiated upon first use of the app only. It will provide the child's name, a starting balance, and a password for the parent to use when making deposits or deductions from the account#
    name = input("What is your child's first name?: ")
    current_balance = int(input("How much money do you want your child's account to start with?: "))
    with open('allowance.csv', 'w', newline='') as allowance_file:
        writer = csv.writer(allowance_file)
        writer.writerow(['Name', 'Amount'])
        writer.writerow([name, current_balance])
    return name, current_balance

def update_balance(child_name, amount):
    with open('allowance.csv',  'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([child_name, amount])

def parent_maintenance(child_name, current_balance):
    #This function will be initiated when a parent uses the app and initial setup has already been completed#
    parent_question = input("Do you want to add or deduct money from the account? Type A or D: ")
    if parent_question == "a":
            add_amount = int(input("How much money do you want to add?: "))
            current_balance = add_amount + current_balance
            print(child_name + "'s current balance is $" + str(current_balance))
            current_balance = update_balance(child_name, add_amount)
            return current_balance
    else:
        if parent_question == "d":
            deduct_amount = int(input("How much money do you want to deduct?: "))
            current_balance = (current_balance - deduct_amount)
            print(child_name + "'s current balance is $" + str(current_balance))
            current_balance = update_balance(child_name, deduct_amount)
            return current_balance

def open_csv(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        current_balance = 0
        child_name = 'Unknown'
        for r in reader:
            child_name = r[0]
            current_balance += int(r[1])
        return child_name, current_balance

def child_maintenance(child_name, current_balance):
    #This function will be initiated when the child uses the app and initial setup has already been completed#
    print("Hi, " + child_name + "!")
    child_question = input("Do you want to check your balance (b) or deduct money (d)?")
    if child_question == "b" or child_question == "B":
            print("Your current balance is $" + str(current_balance))
    else:
        if child_question == "d" or child_question == "D":
            deduct_amount = int(input("How much money do you want to deduct?: "))
            current_balance = (current_balance - deduct_amount)
            print("Your current balance is $" + str(current_balance))
        return current_balance
    return current_balance


if __name__ == '__main__':
    main()
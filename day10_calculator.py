#/home/deepshikha-saanvi/work/git_demo/potential-python-potato

import os
from time import sleep

def add(n1 , n2):
    return n1+n2

def subtract(n1 , n2):
    return n1-n2

def multiply(n1 , n2):
    return n1*n2

def divide(n1 , n2):
    return n1/n2
operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("Here you are! Hop on to use the easy-peasy calculator.... ")
log_history = []

num1 = float(input("Enter the first number: "))

def calculator(num1):
    should_continue = True
    

    while 1:
        if should_continue == True:
            print("Choose an operation: ")
            for operation in operator:
                print(operation)
            symbol = input()

            num2 = float(input("Enter the second number: "))

            output = operator[symbol](num1,num2)
            print(f"{num1} {symbol} {num2} = {output}")
            log_history.append(f"{num1} {symbol} {num2} = {output}")
            sleep(1)
            os.system('clear')

        else:
            see_history = input("Do you want to see calculation history?[y/n] ")
            if see_history == "y":
                for log in log_history:
                    print(log)
            print("See you soon!")
            break

        cont = input("Do you want to continue? [y/n]")
        if cont == "y":
            should_continue = True
            same_output_num = input(f"Do you want to continue with {output} [y/n] ")
            if same_output_num == "y":
                num1 = output
            else:
                num1 = float(input("Enter the first number: "))
        else:
            should_continue = False

    
calculator(num1) 




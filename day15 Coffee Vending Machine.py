# import os
# from time import sleep
#        "sleep(1) // os.system('clear')"
logo = "☕"

#Define Elemental variables
water = 200 # 18 liters
coffee = 100 # 150 g(instant)
milk = 200 # 12 liters
money = 0 
refund  = 0
paid_by_user = 0
type_of_coffee = {'espresso': { 'w' : 50, 'm': 0, 'c': 18, 'mny': 1.5},
                     'latte': { 'w' : 200, 'm': 150, 'c': 24, 'mny':2.5},
                     'cappuccino': { 'w' : 250, 'm': 100, 'c': 24, 'mny': 3.0},}
is_working = True



# Print out the report,  Secret codes - off, report
def report():
        #"""For the maintainers, to check, turn off"""
    global is_working 
    code = input(f"Report/ Off  :").lower()
    if code == "report":
        print(f" \n Water : {water}\n Milk : {milk}\n Coffee : {coffee}\n Profit : {money} \n")
    if code == "off":
        print("Machine Switched off X(")
        is_working = False


#Make a bill, check for amount refund if amount not exact
def negative_refund(amount):
    global money
    money -= amount
    print(f"We have returned, ${amount}, back.")

#Check amount of the ingredients- if not sufficent, reply
def deduct_quantity(drink):
#""" Input - Coffee(Key), Check availabilty, Deduct amount, return 0/1"""
    global water, coffee, milk
    deduct_water = type_of_coffee[drink]['w']
    deduct_milk = type_of_coffee[drink]['m']
    deduct_coffee = type_of_coffee[drink]['c']

    check_water = water - deduct_water
    check_milk = milk - deduct_milk
    check_coffee = coffee - deduct_coffee

    check_items = [check_water,check_milk,check_coffee]
    name_check_items = ['Water','Milk','Coffee']

    finished_item = -1

    for num in range(0,3):
        if check_items[num] < 0:
            finished_item = num

    if finished_item != -1:
        print(f"Sorry, the machine ran out of {name_check_items[finished_item]}")
        
        return 0
    else:
        water = check_water
        milk = check_milk
        coffee = check_coffee
        return 1
        
    


    #Process Dolar coins
def ask_money(drink):
    global money,paid_by_user
    bill = type_of_coffee[drink]["mny"]
    paid_bill = 0
    print(f"Your total bill will be, {bill}")

    penny = 0.01
    nickel = 0.05
    dime = 0.1
    quarter = 0.25

    print("Enter the denominations of your coins")
    paid_bill += 0.01 * (int(input("Penny : ")))
    paid_bill += 0.05 * (int(input("Nickel : ")))
    paid_bill += 0.1 * (int(input("Dime : ")))
    paid_bill += 0.25 * (int(input("Quarter : ")))

    money += paid_bill

    if paid_bill == bill:
        print("Transaction Succesful, lets make your coffee now", {logo})
        paid_by_user = paid_bill
        return 1
    # Depending on the due, refund
    elif paid_bill > bill:
        refund = paid_bill - bill
        money -= refund
        print(f"You gave ${refund} extra, we have refunded it.")
        paid_by_user = paid_bill
        return 1
    else:
        negative_refund(paid_bill)
        return 0


#Make a prompt - Ask which coffee
def choice_of_coffee():
    global water, coffee, milk, money,logo
    choice = input("What would you like? (espresso/latte/cappuccino/#):")
    if choice == "#":
        report()
    else:
        transaction_success = ask_money(choice)
        if transaction_success:
            made_coffee = deduct_quantity(choice)
            if made_coffee:
                print(f"Enjoy your {choice}{logo}")
            else:
                print("We hope to serve you coffee soon :)")
                negative_refund(paid_by_user)
        else:
            print("You can try sometime later :) =) ")

while is_working:
    choice_of_coffee()
    print("\n"*5)





#Clear the screen after the transaction, show home screen.

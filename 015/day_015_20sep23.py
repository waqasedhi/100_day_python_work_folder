MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water=resources["water"]
milk=resources["milk"]
coffee=resources["coffee"]
money=0.0

def report_gen():
    result=f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"
    return result

def itemcheck(water1,milk1,coffee1):
    if water>=water1 and coffee>=coffee1 and milk>=milk1:
        return True
    else:
        if water<water1:
            return "Sorry there is not enough water."
        elif milk<milk1:
            return "Sorry there is not enough milk."
        elif coffee<coffee1:
            return "Sorry there is not enough coffee."


def make_drink(water1,milk1,coffee1,cost1):
    global water,milk,coffee,money
    water-=water1
    milk-=milk1
    coffee-=coffee1
    money+=cost1


def bill_collection(cost1):
    q1=int(input("how many quarters?: ")) 
    q2=int(input("how many dimes?: "))
    q3=int(input("how many nickles?: "))
    q4=int(input("how many pennies?: "))
    collection = (0.25*q1) + (0.1 *q2) + (0.05*q3) + (0.01 *q4)
    if collection>=cost1:
        change=collection-cost1
        print=f"Here is ${change} in change."
        return True, print
    else:
        return "Sorry that's not enough money. Money refunded."
    
    
def cafe():
    print("Wellcome to the CAFE")
    machine_is_on=True
    while machine_is_on:
        #print(report_gen())
        ask=input("What would you like? (espresso/latte/cappuccino):").lower()
        if ask == "espresso" or ask == "latte" or ask == "cappuccino":
            water1=MENU[ask]["ingredients"]["water"]
            milk1=MENU[ask]["ingredients"]["milk"]
            coffee1=MENU[ask]["ingredients"]["coffee"]
            cost=MENU[ask]["cost"]
            #print(type(cost))
            # if ask == "espresso":
            result= itemcheck(water1,milk1,coffee1)
            if result == True:
                print("Please insert coins.")
                amonut=bill_collection(cost)
                if amonut[0]==True:
                    print(amonut[1])
                    make_drink(water1,milk1,coffee1,cost)
                    print(f"Here is your {ask} ☕️. Enjoy!")
                else:
                    print(amonut)
            else:
                print(result)
        
        elif ask =="off":
            machine_is_on=False
        
        elif ask =="report":
            print(report_gen())
        else:
            print("Sorry, wrong entry, bye.")
cafe()

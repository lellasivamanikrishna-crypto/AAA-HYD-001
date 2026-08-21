#day 12

# GRADE CHECKER
marks = int(input("enter marks: "))

# Primary check: Is it a valid score range?
if 0 <= marks <= 100:
    if marks >= 90:
        print('Grade: A')
        print("Outstanding")
    else:
        if marks >= 80:
            print('Grade: B')
            print("Excellent")
        else:
            if marks >= 70:
                print('Grade: C')
                print("Good")
            else:
                if marks >= 60:
                    print('Grade: D')
                    print("Fair, needs to improve")
                else:
                    if marks >= 50:
                        print('Grade: E')
                        print("Poor, needs serious improvement")
                    else:
                        print('Grade: Fail')
                        print("Failed, needs to repair")
else:
    print("Invalid marks entered! Please enter a value between 0 and 100.")

# EVEN-ODD CHECKER 
x = int(input("enter a number: "))

# Primary check: Is it zero?
if x == 0:
    print("Zero is neither even nor odd")
else:
    # Secondary layer: Check for negative values
    if x < 0:
        if x % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")
    # Secondary layer: Check for positive values
    else:
        if x % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

#use case :atm withdrawl senario
#card is valid or not
#entered pin is correct or not
#check the balance
#go for withdrawl
card_Number=input("enter the number:")
pin=int(input("enter the pin:"))
#total_amount,withdrawal_amount=map(int,input("enter the total amount and withdrawal amount").split())
#final_amount=totoal_amount-withdrawal_amount
if card_Number is True:
    if pin ==1234:
        withdrawal_amount=int(input("enter the amount"))
        total_amount=50000
        print(f"the amount of withdrawal:{withdrawal_amount} and the account balance:{total_amount-withdrawal_amount}")
    else:
        print("there is a error in the system please try later")
else:
    print("card inserted is invalid")

card_Number = input("enter the number:")
pin = input("enter the pin:")
withdrawal_amount = int(input("enter the amount: "))
total_amount = 50000
if card_Number.isdigit():
    if pin is True:
        
        if total_amount > withdrawal_amount:
            print(f"the amount of withdrawal:{withdrawal_amount} and the account balance:{total_amount-withdrawal_amount}")
        elif total_amount == withdrawal_amount:
            print(f"the amount of the account balance:{total_amount-withdrawal_amount} please maintain minimum balance for further transactions")
        else:
            
            print("Insufficient funds! You cannot withdraw more than your total balance.")
    else:
        print("card pin is invalid")
else:
    print("card is not in use")

#
budget=int(input("enter the budget:"))
if budget>0:
    if budget>10000:
        print(f"plan:Trip")
    elif budget>5000 and budget<=10000:
        print(f"plan:Resort")
    elif budget>3000 and budget<=5000:
        print(f"plan:Movie and dinner")
    elif budget>1000 and budget<=3000:
        print(f"plan:Cafe and SHOPPING")
    elif budget>500 and budget<=1000:
        print(f"plan:Street Food and park visit")
    else:
        print("please stay home")
else:
    print("no trip amount entered is invalid")



# SEASON IDENTIFIER
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

c = int(input("enter month number: "))

# Primary check: Is it a valid calendar month?
if 1 <= c <= 12:
    if c in winter:
        print("season: Winter")  # Fixed your original 'summer' typo here
    else:
        if c in spring:
            print("season: spring")
        else:
            if c in summer:
                print("season: summer")
            else:
                print("season: Autumn")
else:
    print("Invalid month entered")
#used are if else elif conditonal statemenets and loop to continue the flow with addons as suggestion with the balance amount also
#used break continue to run the loop and exit the loop

balance = 11000
print(f" Welcome! Your starting balance is: ₹{balance}")
while balance > 500:
    budget_input = input("\nEnter how much you want to spend on your next plan (or type 'exit' to quit): ")
    
    if budget_input.lower() == 'exit':
        break
        
    budget = int(budget_input)
    if budget <= 0:
        print("Invalid amount! Please enter a number greater than 0.")
        continue
        
    if budget > balance:
        print(f"You cannot spend ₹{budget}. You only have ₹{balance} left!")
        continue

    if budget > 10000:
        print("Plan Chosen: Grand Trip! ")
    elif 5000 < budget <= 10000:
        print("Plan Chosen: Luxury Resort Stay! ")
    elif 3000 < budget <= 5000:
        print("Plan Chosen: Movie and Premium Dinner! ")
    elif 1000 < budget <= 3000:
        print("Plan Chosen: Cafe Hangout and Shopping! ")
    elif 500 < budget <= 1000:
        print("Plan Chosen: Street Food Feast and Park Visit!")
    else:
        print("That amount is too low for an activity. Please stay home and save!")
        continue 
#continue help us to continue the logic from up and use that logic to make sure we can process that
    balance -= budget
    print(f"Remaining Wallet Balance: ₹{balance}")

    if balance > 10000:
        print("Suggestion: You still have enough left for a full Trip!")
    elif 5000 < balance <= 10000:
        print("Suggestion: You have enough left to book a Resort next!")
    elif 3000 < balance <= 5000:
        print("Suggestion: With your remaining money, you can catch a Movie and Dinner!")
    elif 1000 < balance <= 3000:
        print("Suggestion: You can still hit up a Cafe or go Shopping!")
    elif 500 < balance <= 1000:
        print("Suggestion: You have just enough left for Street Food and a Park stroll!")
    else:
        print("Suggestion: Your balance is low. Time to head home!")

print(f"\nSession Ended. Final savings left over: ₹{balance}")

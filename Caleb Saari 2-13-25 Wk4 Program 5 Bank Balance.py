total_spent = 0

budget =  float(input("Enter the amount you have budgeted for this month: "))

print("Enter your purchases one by one. Once you are done, enter 0")
while True:
    expense = float(input("Enter expense of purchase: "))
    if expense == 0:
        break
    total_spent += expense

difference = budget - total_spent

if difference > 0:
    print("You are under you budget by", difference)
elif difference < 0:
    print("You spent over your budget by", -difference)
else:
    print("You matched you budget of", budget)

#Caleb Saari 2/13/25 Wk4 Program 5 Bank Balance
#Tip calculator
bill=float(input("Welcome to the tip calculator\nWhat was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people=int(input("How many man split the bill? "))
final_amount=bill/people*(tip/100+1)
final_amount=round(final_amount, 2)
final_amount="{:.2f}".format(final_amount)
print("Each person should pay: $", final_amount)
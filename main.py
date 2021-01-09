#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill=float(input("Welcome to the tip calculator\nWhat was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people=int(input("How many man split the bill? "))
final_amount=bill/people*(tip/100+1)
final_amount=round(final_amount, 2)
final_amount="{:.2f}".format(final_amount)
print("Each person should pay: $", final_amount)
def calculate_average (num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average
#def function defines a block of reusable codes
#we write the code once in a function, and call it by the time we need to, instead of writing codes repeatedly.


# This function asks the users for their test scores
print ("Calculating Total Average")
score1 = float(input("Input score: "))
score2 = float(input("Input score: "))
score3 = float(input("Input score: "))


#calls and prints the average of test scores.
final_score = calculate_average (score1, score2, score3)

#prints the result
print (f"Your Final Average Score is: {final_score: .2f}")


print('Meal Cost -- ')
mealCost = float(input())

print('Tip Percent -- ')
tipPercent = int(input())

print('Tax Percent -- ')
taxPercent = int(input())

tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100
totalCost = mealCost + tip + tax
print("The total meal cost is " + str(round(totalCost)) + " dollars.")
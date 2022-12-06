with open("day1/input.txt", "r") as file:
    data = file.read().split("\n")

# Part 1 - Find which elf carries the most calories

caloriesList = []
sumCalories = 0

for item in data:
    if item != "":
        sumCalories += int(item)
    else:
        caloriesList.append(sumCalories)
        sumCalories = 0

maximumCalories = max(caloriesList)
maximumCaloriesElve = caloriesList.index(maximumCalories) + 1

# Part 2 - Find the three elves carrying the most calories

# Using a list

print(caloriesList)

topThreeCalories = []
for i in range(3):
    maxCal = max(caloriesList)
    topThreeCalories.append(maxCal)
    caloriesList.remove(maxCal)

print(topThreeCalories)
print(sum(topThreeCalories))

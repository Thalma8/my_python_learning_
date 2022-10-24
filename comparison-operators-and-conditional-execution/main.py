#
# Write a program that utilizes the concept of conditional execution, takes a string as input, and:
#
# prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

n = input("Enter the name of my favourite plant")
if n == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant")
elif n == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", n, sep=",", end=".")


    # if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
    # if the income was higher than this amount, the tax was equal to 14, 839 thalers and 2 cents, plus 32 % of the surplus over 85, 528 thalers.

    income = float(input("Enter the annual income: "))

    if income < 85528:
        tax = income * 0.18 - 556.02
    else:
        tax = (income - 85528) * 0.32 + 14839.02

    if tax < 0.0:
        tax = 0.0

    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")

    # if the year number isn't divisible by four, it's a common year;
    # otherwise,
    # if the year number isn't divisible by 100, it's a leap year;
    # otherwise,
    # if the year number isn't divisible by 400, it's a common year;
    # otherwise, it
    # 's a leap year.
year = int(input("\n\nEnter a year: "))
if year < 1582:
    print("Not within the grgorian calendar period")
elif year % 4 != 0:
    print("common year")
elif year % 100 != 0:
    print("leap year")
elif year % 400 != 0:
    print("common Year")
else:
    print("leap year")
#counting in missisipily
import time

# Write a for loop that counts to five.
counting = 1
for counting in range(1, 6):
    print("missiaaippi", counting)
    time.sleep(1)
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(0)

# Write a print function with the final message.


print("ready or not here i come")


user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)






# ### Problem 1
# ```
# # Start with this List
# list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```

# Ask the user to enter a number.
userInput = int(input("Enter a number "))

# Using the provided list of numbers, use a for loop to iterate the array and
# print out all the values that are smaller than the user input and print out
# all the values that are larger than the number entered by the user.
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]

for x in list_of_many_numbers:
    # print out all the values that are smaller than the user input
    if (userInput > x):
        print('the value that is smaller than the user input ', x)
    # print out all the values that are larger than the number entered by the user
    if (userInput < x):
        print('the value that is greater than the user input ', x)

# ### Problem 4
# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```

# Write a program that allows users to compare words by their length.
# Implement a function called chk_strings that accepts 2 strings entered
# by the user and compares them by length
def chk_strings():
    str1 = input('Enter a word ')
    str2 = input('Enter another word ')

    # The function should return true if the first string parameter has more
    # characters (i.e. longer) than the second string passed into the function,
    if (str2 > str1):
        return 'true'
    # otherwise, the function should return false.
    else:
        return 'false'

# DO NOT print the result in the function, print the result using the return
# value provided by the function.
print(chk_strings())







# TODO: figure out how to take str input and return only the number

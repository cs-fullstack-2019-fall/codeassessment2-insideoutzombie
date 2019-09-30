# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2
# lists provided to produce a new list by alternating values between the 2 lists.
# Once the merge has been completed, print the new list of claim numbers
# (DO NOT just print the array variable!)
# ```
# # Start with these lists
# list_of_claim_nums_1 = [2, 4, 6, 8, 10]
# list_of_claim_nums_2 = [1, 3, 5, 7, 9]
# ```
# Example Output:
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# ```

# empty array to pass the data into
merge_array = []

list_of_claim_nums_1 = [2, 4, 6, 8, 10]
list_of_claim_nums_2 = [1, 3, 5, 7, 9]

# declare a function
def someFun():
    # loop to cycle through the list1 array
    for x in list_of_claim_nums_1:
        # adds the array to the empty array
        merge_array.append(x)
    # loop to cycle through the list2 array
    for y in list_of_claim_nums_2:
        # adds the array to the empty array
        merge_array.append(y)

    return merge_array

print(someFun())

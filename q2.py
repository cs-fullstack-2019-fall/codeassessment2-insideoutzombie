# ### Problem 2

# Prompt the user with the message, ‘Is it better to be rude or kind to People?’
userInput = input('Is it better to be rude or kind to People? ')

# Keep prompting the user to enter an answer until they enter the word kind.
while(userInput != 'kind'):
    # Each time they enter something other than kind, print the message,
    # ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
    userInput = input('That’s not the answer I had hoped to hear. Try again. ')
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the programself.
print('Now that’s what I wanted to hear!')

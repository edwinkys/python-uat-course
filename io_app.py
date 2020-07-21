'''

This is the tutorial to create a function in Python

'''

def divider(n=10):
    '''
    Function to print divider line.
    '''
    print('-' * n)

# Displaying a text
print('\n\nThis tutorial will show you how to create a function\n')
divider()

print('\nYou use \'def\' followed by the function name.\n\nFunction is used to avoid code repetition just like my divider line here.\n\nAfter you create a function, you can call the function wherever you need it.\n')
divider()

# Prompt for user input
n_dash = int(input('\nGive a number of how many dash per divider line: '))
n_line = int(input('How many lines do you want to create: '))

# Initialize list for looping
n_line = range(n_line)

for i in n_line:
    divider(n_dash)

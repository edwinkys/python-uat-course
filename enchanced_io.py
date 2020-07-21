'''

This is the code tutorial on how to create an omellete.

'''

print('''# # # # # # # # # #
Welcome to the tutorial on how to create an omellete.

In this tutorial, you will learn to create a great omellete.
# # # # # # # # # #''')

# Ask for user's name
name = ''

# Loop if the user doesn't input any name
while len(name) is 0:
    name = str(input('\nWhat should I call you? '))

print('\nWelcome to the tutorial {name}!'.format(name=name))

# Prompt the number of eggs
n_eggs = int(input('How many eggs do you want to cook? '))

# If statement
if n_eggs <= 0:
    print('[ERROR] The number of eggs can\'t be less than or equal to 0')
    print('[ERROR] Exiting the program...')
else:
    if n_eggs > 0 and n_eggs <= 5:
        for i in range(n_eggs):
            print('Cooking {} egg'.format(i+1))
    
        print('[SUCCESS] Well done! You have create {} eggs!'.format(n_eggs))
    else:
        print('[ERROR] The number of eggs are too many')
        print('[ERROR] Exiting the program...')

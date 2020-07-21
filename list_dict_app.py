'''

This is the code tutorial on how to create an egg dish.

'''

print('''# # # # # # # # # #
Welcome to the tutorial on how to create an egg dish.

In this tutorial, you will learn to create a great egg dish.
# # # # # # # # # #''')

# Ask for user's name
name = ''

# Loop if the user doesn't input any name
while len(name) is 0:
    name = str(input('\nWhat should I call you? '))

print('\nWelcome to the tutorial {name}!'.format(name=name))

# Prompt the number of eggs
n_eggs = int(input('How many eggs do you want to cook? '))

# List of type of eggs
type_eggs = ['boiled egg(s)', 'omellette(s)', 'fried egg(s)']

# How many minutes does it take to cook 1 of the egg dishes
type_to_duration = {
    type_eggs[0]: 5,
    type_eggs[1]: 3,
    type_eggs[2]: 2
}

egg_dish = int(input('''What type of egg dish you like to cook?
0. Boiled Egg
1. Omellette
2. Fried Egg
Your choice: '''))

# If statement
if n_eggs <= 0:
    print('[ERROR] The number of eggs can\'t be less than or equal to 0')
    print('[ERROR] Exiting the program...')
else:
    if n_eggs > 0 and n_eggs <= 5:
        for i in range(n_eggs):
            print('Cooking {} egg'.format(i+1))
    
        print('[SUCCESS] Well done! You have create {} {} in {} minutes'.format(n_eggs, type_eggs[egg_dish], n_eggs * type_to_duration[type_eggs[egg_dish]]))
    else:
        print('[ERROR] The number of eggs are too many')
        print('[ERROR] Exiting the program...')

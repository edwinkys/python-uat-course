'''

This is a text adventure program in Python

'''


def welcome():
    '''
    
    The function to welcome the new player
    
    return: None
    
    '''
    print('Welcome to Rock Adventure.')
    print('In this game you will be a rock to save the Elven Forest and be the best in the world.\n')


def stage_1(inventory=[]):
    '''
    
    The function to trigger stage 1 of the game
    
    @inventory: List of items in inventory
    
    return: None
    
    '''
    
    print('You are a newly born rock in an Elven Forest.')
    print('Your goal is to become the best rock in the world.\n')

    print('What would you do?')
    print('1. Converse with another rock nearby')
    print('2. Sleep for another 100,000 years')
    
    # Inventory
    print('\nInventory: ', end='')
    for item in inventory:
        print(item, end='   ')


def stage_2(inventory=[]):
    '''
    
    The function to trigger stage 2 of the game
    
    @inventory: List of items in inventory
    
    return: None
    
    '''
    
    print('You conversed to a nearby rock and found out that he is a wizard.')
    print('He gave you several of his magic item and he asked you to save the forest from the Evil Elven Council.')
    print('You obtained Ultra Laser, Teleportation, and Levitation\n')

    print('What would you do?')
    print('1. Teleport to Elven Council Hall')
    print('2. Ignore the old man wish and chill')
    
    # Inventory
    print('\nInventory: ', end='')
    for item in inventory:
        print(item, end='   ')


def stage_3(inventory=[]):
    '''
    
    The function to trigger stage 3 of the game
    
    @inventory: List of items in inventory
    
    return: None
    
    '''
    
    print('You arrived in the council hall to confront the elder wizard.')
    print('You have some skills left to use against the elder wizard.\n')

    print('What would you do?')
    print('1. Use Ultra Laser to attack the wizard')
    print('2. Use Levitation to evade the wizard attack')
    
    # Inventory
    print('\nInventory: ', end='')
    for item in inventory:
        print(item, end='   ')


def victory(inventory):
    '''
    
    Trigger winning stage.
    
    return: None
    
    '''
    
    print('Congratulations!')
    print('The wizard used Explosion and blow up the council hall.')
    print('The ceiling fell down onto the wizard killing the wizard.')

    # Write a file for the winner
    with open('trophy.txt', 'a') as f:
        f.write('Congratulations for your completion of the story!\n')
        f.write('You are now the best rock in the world and you successfully save the Elven forest\n')
        f.write('Here is the left of the wizardry skill that you still possess: ')

        # List every items the user have
        for item in inventory:
            f.write(item + ', ')

def losing():
    '''
    
    Trigger losing stage.
    
    return: None
    
    '''
    
    print('Game Over!')
    print('You are killed by the Elven Council Wizard')

def remove_item_from_inventory(item, inventory):
    '''
    
    The function to remove an item from the inventory.
    
    @item: The string of the item
    @inventory: The list of the items in inventory
    
    return: inventory
    
    '''
    
    inventory.remove(item)
    
    return inventory


def start_game():
    '''
    
    Function to start the game.
    
    return: None
    
    '''

    inventory = []

    welcome()
    
    # Stage 1
    stage_1()
    user_input = int(input('\nChoose the action you would do (1 or 2): '))
    print('\n')
    if user_input is 1:
        inventory = ['Ultra Laser', 'Teleportation', 'Levitation']
        stage_2(inventory)
        user_input_2 = int(input('\nChoose the action you would do (1 or 2): '))
        print('\n')
        
        if user_input_2 is 1:
            inventory = remove_item_from_inventory('Teleportation', inventory)
            stage_3(inventory)
            user_input_3 = int(input('\nChoose the action you would do (1 or 2): '))
            print('\n')
            
            if user_input_3 is 2:
                remove_item_from_inventory('Levitation', inventory)
                victory(inventory)
            
            else:
                losing()

        else:
            losing()
        
    else:
        losing()
    

# Run the game
start_game()
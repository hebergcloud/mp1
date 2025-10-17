from gaming_tools import*

def special_ability(character:str,target:str):
    """each character has a special ability that he gonna use .
    
    Parameters
    =========
    character : the name of the character (str).
    target: the name of the target (str).
    
    """
    #We see if the character exists

    if character_exists(character):
        variety = get_character_variety(character)
        if character_alive(character) : 
            if variety=='necromancer':
                necromancer_power(target)
            elif variety =='wizard':
                wizard_power(target) 
            elif variety =='healer':
                healer_power(target)
            else:
                print('The character does not have a special ability.')
        else:
            print('The character is dead. Can not use special ability.')   
    else:
        print('The character does not exist.')

def necromancer_power(target:str):
    """Let the necromancer revive the target with 10 points of live for 75 pieces of gold.

    Parameter
    =========
    target : the name of the character we want to revive (str)
    
    """
    
    # Checks if the target exist
    if character_exists(target):
        
        # Checks if the team has enough money
        if get_team_money()>=75:
            if character_alive(target)==False :
                set_character_life(target,10)
                set_team_money(get_team_money()-75)
            else:
                print('The character is not dead.')
        else:
            print('Not enough money.')
    else:
        print('The character does not exist.')
def wizard_power(target:str):
    """Let the wizard reduce the live of the creature  by half for 20 pieces of gold.
     
     Parameters
     =========
     target: the name of the creature (str).
     """
     
     #check if the creature exists
    if creature_exists(target):
        if get_team_money()>=20:
            set_creature_life(target,get_creature_life(target)//2)
            set_team_money(get_team_money()-20)
        else:
            print('Not enough money.')
    else:
        print('The creature does not exist.')  
def healer_power(target:str):
    """Lets the healer heal a character in the team for 10 pieces of gold
    
    Parameters
    =========
    target : the name of the character we heal
    """  
    # Checks if the target exists 
    if character_exists(target):
        if get_team_money()>=5:
            if character_alive(target):
                set_character_life(target,get_character_life(target)+10)
                set_team_money(get_team_money()-5)
            else:
                print('The character is dead. Can not heal.')
        else:
            print('Not enough money.')
    else: 
        print('The character does not exist.')
    
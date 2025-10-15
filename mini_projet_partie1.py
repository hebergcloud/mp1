from gaming_tools import *
from random import randint
reset_game()
def give_money(money:int):
    """
    Give the money to the team.
    Parameters
    ==========
    money : int
        The amount of money given to the team.
    """
    set_team_money(money)
    print("The team now has :", money)
give_money(50)
def create_character(character:str,variety:str):
    """
    Allow the player to creat a character.
    Creates a character with player_life, strength and reach depends on the variety of the creature .
    Parameters
    ==========
    character: Name of the character (str).
    variety: the type of the character(dwarf,nécromancien,wizard,soignant)(str).
    return
    ======
    character: Name of the character (str).
    variety: the type of the character(dwarf,nécromancien,wizard,soignant)(str).
    strenght: the strenght of the character(str). 
    player_life:the life of the character(int).
    reach : the reach of the character ('longue','short').
"""
    if character_exists(character)==True:
         print('the character already exist')
    else:
    # the player can chose the name and the variety
        if   variety=='dwarf':
             strength=randint (10,50)
             player_life=randint (10,50)
        elif variety=='elfe':
             strength=randint(15,25)
             player_life=randint(15,25)
        elif variety in ['healer', 'wizard', 'nécromancien']:
             strength=randint(5,15)
             player_life=randint(5,15)
    #find the reach
        if variety in ['healer', 'wizard', 'nécromancien']:
             reach='short reach'
        else:
             reach='longue reach'
    print('the character is created his name is:',character,'\n his variety is :',variety,'\n his strenght is :',strength,'\n his life is :',player_life,'\n his reach is :',reach)
create_character('malak','dwarf')

def upgrade_character(character:str,money:int):
    """
    Allow a player to evolve their character for 4 gold coins.
    There is a 25% chance to increase strength by 4,
    and a 50% chance to increase life by 2.
    Both improvements are independent and can happen together.

    Parameters
    ----------
    character: Name of the character (str).
    money: the amount of money of the team(int).
    cost:the cost of the upgrade(int).
    """
    cost=4
    if character_exists(character)==False:
         print('the character does not exist there will be no modification')
    else:
         #verify if the money is enough
         if money < cost:
             print('the player does not have enough money ')
             return 
         else:
             player_life = get_character_life(character)
             strength = get_character_strength(character)
             set_character_life(character)
             # 25% chance to develop his strength
             if randint(1, 100) <= 25:
                 strength += 4
                 set_character_strength(character, strength)
                 print('strength increases by 4:',strength)
             # 50% de chance d’augmenter la vie
             if randint(1, 100) <= 50:
                 player_life += 2
                 set_character_life(character,player_life)
                 print('life increases by 2:',player_life)
             else:
                 print('there is no evolution ')
    set_team_money(money)
    money-= cost
    print('the money left is:',money)

    upgrade_character('malak',13)

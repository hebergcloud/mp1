from gaming_tools import *
from random import randint

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
    variety: the type of the character(dwarf,necromancien,wizard,healer)(str).
    return
    ======
    character: Name of the character (str).
    variety: the type of the character(dwarf,necromancien,wizard,healer)(str).
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
        elif variety in ['healer', 'wizard', 'necromancien']:
             strength=randint(5,15)
             player_life=randint(5,15)
    #find the reach
        if variety in ['healer', 'wizard', 'necromancien']:
             reach='short'
        else:
             reach='long'
        print(' the character is created his name is:',character,'\n his variety is :',variety,'\n his strenght is :',strength,'\n his life is :',player_life,'\n his reach is :',reach)
        add_new_character(character, variety,reach,strength,player_life)


def upgrade_character(character:str):
    """
    Allow a player to evolve their character for 4 gold coins.
    There is a 25% chance to increase strength by 4,
    and a 50% chance to increase life by 2.
    Both improvements are independent and can happen together.

    Parameters
    ----------
    character: Name of the character (str)
    cost:the cost of the upgrade(int).
    """
    cost=4
    money = get_team_money()
    if character_exists(character)==False:
         print('the character does not exist there will be no modification')
    else:
         #verify if the money is enough
         if money < cost:
             print('the player does not have enough money ')
             return 
         else:
             player_life = get_character_life(character)
             print(player_life)
             strength = get_character_strength(character)
             print(strength)
             set_character_life(character,player_life)
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
    money-= cost
    set_team_money(money)
    print('the money left is:',money)

def use_special_ability(name: str ) ->str:
    """This function will be useful for using strengths against gold coins.

    Parameters
    ----------
    type : str
        the players name

    Returns
    -------
    str
        return the strength to use and the remaining gold after using the strength
    """


def create_creature():
    """Create a new creature
    """
    if is_there_a_creature() == True:
        print("a creature already exists")
    else:

        life = random.randint(1,10) * (1+int(get_nb_defeated()))
        strength = random.randint(1,10) * (1+int(get_nb_defeated()))

        if random.randint(0,1) == 1:
            reach = "short"
        else:
            reach = "long"

        creature = get_random_creature_name()
        add_creature(creature, reach, strength, life)

        print("The new creature is named ", creature , " avec ", reach , " de porter , elle ferra " , strength, " de degat et il a ",life, " de vie")

def attack(name_character: str, name_creature: str):
    """Attak character vs attack creature

    Parameters
    ----------
    name_character : str
        _description_
    name_creature : str
        _description_
    """

    if creature_exists(name_creature) and character_exists(name_character):

        # On regarde si la portée de la creature et du character sont tous les 2 long ou court alors ....  
        if (get_character_reach(name_character) == "long" and get_creature_reach(name_creature) == "long") or (get_character_reach(name_character) == "short" and get_creature_reach(name_creature) == "short"):
            # Il y a une variable qui se crée avec la vie actuel de la creature moins la force du character
            life_creature = get_creature_life(name_creature) - get_character_strength(name_character)
            life_character = get_character_life(name_character) - get_creature_strength(name_creature)
            # si la vie de la creature est inferieur à 0 alors on set la vie à 0
            if life_creature < 0:
                set_creature_life(name_creature, 0)
            if life_character < 0:
                set_character_life(name_character, 0)
            if life_creature >= 0: 
                set_creature_life(name_creature,life_creature)
            if life_character >= 0:    
                set_character_life(name_character,life_character)

            if get_creature_life(name_creature) == 0:
                money = get_team_money() + 40 + 10 * (get_nb_defeated()+1)
                set_team_money(money)
                print("The creature is Dead")
                print("Il vous reste actuellement " + str(get_character_life(name_character)) + " De vie")
                print("Vous avez donc maintenant %d d'argent dans votre pot communs" % get_team_money())
                remove_creature(name_creature)
            else: 
                print("La creature à mainenant plus que " + str(get_creature_life(name_creature)) + " De vie")
                if life_character == 0:
                    print("Vous êtes dead")
                else:
                    print("Il vous reste actuellement "+ str(get_character_life(name_character)) + " de vie")

        elif get_character_reach(name_character) == "short" and get_creature_reach(name_creature) == "long":
            raise ValueError("Votre personnage n'est pas en mesure d'attaquer la creature")
        
        elif get_character_reach(name_character) == "long" and get_creature_reach(name_creature) == "short":
            life_creature = get_creature_life(name_creature) - get_character_strength(name_character)
            if life_creature < 0:
                set_creature_life(name_creature, 0)
            elif life_character < 0:
                set_character_life(name_character, 0)

            if get_creature_life(name_creature) == 0:
                money = get_team_money() + 40 + 10 * (get_nb_defeated()+1)
                set_team_money(money)
                print("The creature is Dead")
                print("Vous avez donc maintenant %d d'argent dans votre pot communs" % get_team_money())
                remove_creature(name_creature)

            else: 
                print("La creature à mainenant plus que " + str(get_creature_life(name_creature)) + " De vie vous avez pris aucun dégat car la creature est à courte portée")

    else: 
        print("Le nom de la creature ou du joueur n'exite pas ")


create_character("Nono","healer")
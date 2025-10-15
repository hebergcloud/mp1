from gaming_tools import *
from creature import *
from character import *

def attack(name_character: str, name_creature: str):
    """Attack character vs attack creature

    Parameters
    ----------
    name_character : str
        _description_
    name_creature : str
        _description_
    """

    if creature_exists(name_creature) and character_exists(name_character):

        # We check if the range of the creature and the character are both long or short, then....  
        if (get_character_reach(name_character) == "long" and get_creature_reach(name_creature) == "long") or (get_character_reach(name_character) == "short" and get_creature_reach(name_creature) == "short"):
            # There is a variable that is created with the creature's current life minus the character's strength.
            life_creature = get_creature_life(name_creature) - get_character_strength(name_character)
            life_character = get_character_life(name_character) - get_creature_strength(name_creature)
            # if the creature's life is less than 0, then set life to 0.
            if life_creature =< 0:
                set_creature_life(name_creature, 0)
            if life_character =< 0:
                set_character_life(name_character, 0)
            if life_creature >= 0: 
                set_creature_life(name_creature,life_creature)
            if life_character >= 0:    
                set_character_life(name_character,life_character)

            if get_creature_life(name_creature) == 0:
                money = get_team_money() + 40 + 10 * (get_nb_defeated()+1)
                set_team_money(money)
                print("The creature is Dead")
                print("You currently have " + str(get_character_life(name_character)) + " of life")
                print("So now you have %d money in your common pot" % get_team_money())
                remove_creature(name_creature)
            else: 
                print("The creature now more than " + str(get_creature_life(name_creature)) + " of life")
                print("You currently have "+ str(get_character_life(name_character)) + " of live")

        elif get_character_reach(name_character) == "short" and get_creature_reach(name_creature) == "long":
            print("Your character is unable to attack the creature.")
        
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
                print("So now you have %d money in your common pot" % get_team_money())
                remove_creature(name_creature)
            else: 
                print("The creature now more than" + str(get_creature_life(name_creature)) + "You took no damage because the creature is within short range.")

    else: 
        print("The name of the creature or player does not exist.")


create_creature()


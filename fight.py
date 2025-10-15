from gaming_tools import *
from creature import *
from character import *

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
                print("Il vous reste actuellement "+ str(get_character_life(name_character)) + " de vie")

        elif get_character_reach(name_character) == "short" and get_creature_reach(name_creature) == "long":
            print("Votre personnage n'est pas en mesure d'attaquer la creature")
        
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

create_creature()
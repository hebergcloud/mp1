from gaming_tools import *
import random


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
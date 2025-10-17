from gaming_tools import*



def abilities(character_name: str, target_name: str, type_action: str):
    """
    When a player wants to use his ability besides his attack.
    
    Parameters:
    
    character_name (str) : name of the character who uses his ability.
    target_name (str) : name of the character that receives the ability. 
    type_action (str) : the type of ability of the character. 
    
    """
    if type_action == "healer":
        if get_character_life <= 0:
            print("The target_name is dead and can't be healed.")
        if get_team_money <= 5:
            print("The character_name doesn't have enough gold.")
        else :
            print("character_name heal target_name of 10 hp.")
        return
        get_character_life + 10
        get_team_money - 5
    
    elif type_action == "wizard": 
        if get_creature_life <= 0: 
            print("The creature is already dead so the ability can't be used.")
        if get_team_money < 20:
            print("The character_name doesn't have enough gold.")
        else:
            print("The character_name cast a spell on target_name.")
        return
        get_creature_life //2
        get_team_money -20

    elif type_action == "necromencer":
        if get_character_life > 0:
            print("The character_name is alive so the ability can't be used.")
        if get_team_money < 75:
            print("The Character_name doesn't have enough gold.")
        else: 
            print("The character_name brings back to life target_name.")
        return
        get_character_life + 10
        get_team_money - 75
    else:
        print("Type of action unknown.")





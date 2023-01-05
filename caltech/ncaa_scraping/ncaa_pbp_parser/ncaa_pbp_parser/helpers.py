import re

def list_to_string(list):
    return ', '.join(list)

def string_to_list(string):
    if string == None:
        return []
    if string == '':
        return []
    return string.split(', ')

def find_player(text):
    pattern = r"\b[a-zA-Z]+, [a-zA-Z]+\b"
    matches = re.findall(pattern, text)
    
    if len(matches) == 0:
        return ""
    
    player = matches[-1]
    last, first = player.split(",")
    return first.upper()[1:] + ' ' + last.upper()

def add_player_to_list_retro(row, player, is_home, idx):
            
    if row.name > idx:
        return
    
    lineup_column = "visitorPlayers"
    if is_home:
        lineup_column = "homePlayers"
    
    lineup_list = string_to_list(row[lineup_column])
    
    if player not in lineup_list:
        lineup_list.append(player)
    
    row[lineup_column] = list_to_string(lineup_list)
    
    return row
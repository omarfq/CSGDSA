# Write a function that accepts two arrays of players and returns an array of the players who play in
# both sports
def find_common_players(players_array_1, players_array_2):
    common_players_hash_table = {}
    common_players_array = []
    for player in players_array_1:
        common_players_hash_table[player['first_name']] = player['last_name']

    for player in players_array_2:
        if player['first_name'] in common_players_hash_table.keys():
            common_players_array.append()

    return common_players_array


test = {}

basketball_players = [
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},
    {'first_name': "Janko", 'last_name': "Barton", 'team': "Sharks"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Sharks"},
    {'first_name': "Jill", 'last_name': "Moloney", 'team': "Gators"},
    {'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"}
]

football_players = [
    {'first_name': "Hanzla", 'last_name': "Radosti", 'team': "32ers"},
    {'first_name': "Tina", 'last_name': "Watkins", 'team': "Barleycorns"},
    {'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Barleycorns"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Barleycorns"}
]

print(find_common_players(basketball_players, football_players))

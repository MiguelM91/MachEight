import requests
import json
from typing import Dict, List, Tuple
from requests.models import HTTPError


URL = "https://mach-eight.uc.r.appspot.com/"


def retrieve_players_info():
    """Function to retrieve NBA players information
    from https://mach-eight.uc.r.appspot.com/ API
    """
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.json().get("values")
    else:
        raise HTTPError("API not available")
    return content


def extract_player_info(players: List[Dict]) -> Tuple[List, List]:
    heigths_list = [int(player.get("h_in")) for player in players]
    names_list = [
        f"{player.get('first_name')} {player.get('last_name')}" for player in players
    ]
    return (heigths_list, names_list)


def search_pairs(players_heights, sum):
    aux_hash_table = {}
    found_pairs = []
    for i, player_height in enumerate(players_heights):
        difference = sum - player_height
        if difference not in aux_hash_table:
            aux_hash_table[player_height] = i
        else:
            found_pairs.append(((aux_hash_table[difference], i)))
    return found_pairs


def correlate_pairs_and_names(pairs: List[Tuple], names: List[str]) -> List[Tuple]:
    final_list = []
    for i, pair in enumerate(pairs):
        names_tuple = (names[pair[0]], names[pair[1]])
        final_list.append(names_tuple)
    return final_list


def detecting_sum_of_heights(expected_sum: int):

    '''This is the handler that will orchestrate
    the entire logic
    '''

    # Retrieves the data from the API
    players_info = retrieve_players_info()

    # Extracts the heigths and the names from the retrieved data
    (players_heights, players_names) = extract_player_info(players_info)
    
    # Finding the pairs of players that sums up the expected sum integer
    pairs = search_pairs(players_heights, expected_sum)
    
    # Correlate index pairs with players names pairs
    pairs_of_names = correlate_pairs_and_names(pairs, players_names)
    return pairs_of_names


if __name__ == "__main__":
    sum = 139
    result = detecting_sum_of_heights(sum)
    print(result)

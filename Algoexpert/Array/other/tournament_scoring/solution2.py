#This is inspired by AlgoExpert.io
#Tournament Winner
#The soultion complexity is O(n) time | O(k) space
#n is the number of competitions
#k is the number of teams


from typing import List

HOWME_TEAM_WON = 1
POINTS = 3

def tournment_winner(competitions: List[List[str]], results: List[int]) -> str:
    """Get the winner of the tournament
    
    Args:
        competitions: A list of lists of two teams
        results: A list of integers representing the winner of each competition 1 means home team won and 0 means away team won
    Returns:
        The winner of the tournament
    Raises:
        Exception: If the number of competitions is not equal to the number of results or type of the input is not correct
    """
    if not isinstance(competitions, list) or not isinstance(results, list):
        raise Exception("The type of the input is not correct")

    if len(competitions) != len(results):
        raise Exception("The number of competitions is not equal to the number of results")
    
    current_best_team = ""
    winner_dict = {current_best_team: 0}
    for index, teams in enumerate(competitions):
        home_team , away_team = teams
        res = results[index]
        current_team = home_team if res == HOWME_TEAM_WON else away_team
        update_winner_dict(current_team, winner_dict)
        if winner_dict[current_team] > winner_dict[current_best_team]:
            current_best_team = current_team

    return current_best_team

def update_winner_dict(current_team: str, winner_dict: dict):
    if current_team in winner_dict:
        winner_dict[current_team] += POINTS
    else:
        winner_dict[current_team] = POINTS




if __name__ == '__main__':
    compition = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournment_winner(compition, results))
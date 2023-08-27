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

	winner_dict = {}
	winner = None
	for index, teams in enumerate(competitions):
		home_team , away_team = teams
		if results[index] == HOWME_TEAM_WON:
			winner = home_team
		else:
			winner = away_team


		if winner in winner_dict:
			winner_dict[winner] += POINTS
		else:
			winner_dict[winner] = POINTS


	the_best_score_team = max(winner_dict, key=winner_dict.get)

	return the_best_score_team


	


if __name__ == '__main__':
    compition = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournment_winner(compition, results))








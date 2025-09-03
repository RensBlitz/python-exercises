# exercises/leaderboard.py

from typing import List, Dict, Any


def top_three(players: List[Dict[str, Any]]) -> List[str]:
    """
    Process a list of players with their scores and return the top 3.

    This function should:
    - Take a list of player maps, each containing "name" and "points"
    - Sort the players by their points (highest first)
    - Select the top 3 players
    - Format the output as "1. Name (pts)", "2. Name (pts)", etc.

    Think about: How do you sort items by a specific field? How do you extract values from maps?
    What happens if there are fewer than 3 players? How do you format strings with numbers?

    TODO: Implement top 3 player selection and formatting
    """
    raise NotImplementedError()

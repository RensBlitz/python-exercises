# exercises/simple_dungeon_crawler.py

def simulate(actions: list[str]) -> int:
    """
    Start with health = 5. For each action in order:
      - "hit"    → decrease health by 1
      - "potion" → increase health by 2
    Return the final health after processing all actions.

    Example (from tests):
      actions = ["hit", "potion", "hit", "hit"]
      health: 5 → 4 → 6 → 5 → 4 → return 4
    """
    raise NotImplementedError() 
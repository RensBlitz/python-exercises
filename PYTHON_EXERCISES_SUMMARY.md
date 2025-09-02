## Python Exercises Summary

This document provides an overview of all the Python exercises in the `exercises` package, including their names and what needs to be implemented.

### Exercise List

1. **amusement_park_ticket.py** — `compute_price(age: int, base_price: float) -> float`
   - Calculate ticket price: under 18 or at least 65 → 0.0, otherwise pay `base_price`.

2. **bank_fee_simulator.py** — `simulate_transactions(initial_balance: float, number_of_transactions: int) -> float`
   - Each transaction costs $0.50. Transactions beyond the first 10 also incur $0.30 extra each. Return final balance.

3. **book_page_estimator.py** — `estimate_pages(pages_per_hour: int, minutes: int) -> float`
   - Compute pages read: `pages_per_hour * minutes / 60`.

4. **cafe_tip_jar.py** — `total_with_tip(bill: float, tip_percent: float) -> float`
   - Return bill plus `tip_percent` percent.

5. **classroom_scores.py** — `average(scores: list[int]) -> float`
   - Return average of integer scores. List is non-empty per tests.

6. **contact_book.py** — `to_map(contacts: list[tuple[str, str]]) -> dict[str, str]`
   - Convert `(name, phone)` tuples into a `name → phone` dictionary.

7. **elevator_panel.py** — `is_valid_floor(floor: int) -> bool`
   - Valid floors are 0 through 20 inclusive.

8. **even_odd_game.py** — `classify(n: int) -> str`
   - Return "wizard" for even, "orc" for odd.

9. **fantasy_potion_mix.py** — `ingredient_volumes(vial_ml: int) -> list[int]`
   - Compute [30%, 50%, 20%] of vial_ml as integers that sum to vial_ml.

10. **file_statistics.py** — `lines_and_words(file_path: str) -> tuple[int, int]`
   - Count lines and whitespace-delimited words in a UTF-8 text file.

11. **fizz_buzz_lite.py** — `generate() -> list[str]`
   - First 20 items of FizzBuzz with only 3-multiples as "Fizz" checked in tests.

12. **game_leaderboard.py** — `top_players(scores: dict[str, int]) -> list[str]`
   - Return player names sorted by descending score.

13. **grade_average.py** — `average(a: float, b: float, c: float) -> float`
   - Arithmetic mean of three values.

14. **gradebook.py** — `Student` dataclass, `top_student(students: list[Student]) -> str`
   - Return the name of the student with the highest grade.

15. **hello_hero.py** — `greet(name: str) -> str`
   - Return `"Welcome, {name}!"`.

16. **inventory_tracker.py** — `update_inventory(inventory: dict[str, int], purchases: dict[str, int]) -> dict[str, int]`
   - Subtract purchased quantities; return a new dict.

17. **leaderboard_manager.py** — `update_top_three(current: list[int], new_score: int) -> list[int]`
   - Insert `new_score` into descending top-3 if applicable; return updated list.

18. **library.py** — `is_available(inventory: list[str], book: str) -> bool`
   - Return whether `book` exists in `inventory`.

19. **matrix_transpose.py** — `transpose(matrix: list[list[int]]) -> list[list[int]]`
   - Return the transpose of a 2D matrix.

20. **mini_rpg.py** — `simulate_battle(initial_health: int, damages: list[int]) -> int`
   - Subtract each damage; return final health.

21. **moon_weight_converter.py** — `to_moon_weight(earth_weight: float) -> float`
   - Multiply by 0.165.

22. **order_processor.py** — `total_with_free_shipping_for_big_orders(orders: list[float]) -> float`
   - Return sum if total ≥ 100.0, else 0.0.

23. **parking_lot.py** — `turned_away(max_capacity: int, arrivals: list[int]) -> int`
   - Count vehicles beyond capacity.

24. **pizza_planner.py** — `pizzas_needed(guests: int, slices_per_pizza: int) -> int`
   - Ceiling division to cover all guests (1 slice/person in tests).

25. **plant_watering_schedule.py** — `should_water(day_name: str) -> bool`
   - True only for "Monday".

26. **pocket_money_tracker.py** — `calculate_total(monday_amount: int, wednesday_amount: int) -> int`
   - Sum both amounts.

27. **rain_streak_counter.py** — `longest_streak(rain_days: list[bool]) -> int`
   - Longest consecutive True streak.

28. **shopping_basket.py** — `calculate_total(prices: list[float]) -> float`
   - Sum the list of prices.

29. **simple_dungeon_crawler.py** — `simulate(actions: list[str]) -> int`
   - Start at 5 HP; "hit": -1, "potion": +2; return final HP.

30. **space_probe_signal_time.py** — `round_trip_seconds(one_way_km: float) -> float`
   - `(2 * one_way_km) / 299_792.0`.

31. **speed_unit_switcher.py** — `miles_to_km_per_hour(mph: float) -> float`
   - Convert mph to kph using 1.60934.

32. **student_grades.py** — `average_grades(records: dict[str, list[float]]) -> dict[str, float]`
   - Map students to the average of their grades.

33. **student_records.py** — `top_students(records: dict[str, str]) -> list[str]`
   - Names with grade "A" in iteration order.

34. **temperature_spread.py** — `spread_and_average(high: float, low: float) -> tuple[float, float]`
   - Return `(high - low, (high + low) / 2)`.

35. **tiny_encryption.py** — `encrypt(text: str, key: int) -> str`
   - Shift each character by key positions (simple Caesar in tests).

36. **tip_calculator.py** — `calculate_tip_in_cents(bill_cents: int, tip_percent: int) -> int`
   - `bill_cents * tip_percent / 100` rounded to nearest int cents.

37. **todo_list.py** — `pending_tasks(tasks: list[str], completed_indices: list[int]) -> list[str]`
   - Return tasks whose indices are not in `completed_indices`.

38. **vat_calculator.py** — `add_vat(amount: float, vat_percent: float) -> float`
   - Return `amount + amount * vat_percent / 100`.

39. **word_counter.py** — `count_words(sentence: str) -> dict[str, int]`
   - Whitespace-split and count words case-sensitively.



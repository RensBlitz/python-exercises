# Python Programming Exercises

This repository contains 40 Python programming exercises designed to help students learn and practice Python fundamentals. Each exercise consists of a function stub that raises `NotImplementedError()` and corresponding test cases.

## 📚 Exercise Categories

### 1️⃣ Variables & Primitive Data Types (8 exercises)
- **pocket_money_tracker**: Basic arithmetic operations
- **cafe_tip_jar**: Percentage calculations
- **moon_weight_converter**: Constants and multiplication
- **book_page_estimator**: Time and rate calculations
- **temperature_spread**: Tuple returns and multiple calculations
- **space_probe_signal_time**: Scientific calculations
- **fantasy_potion_mix**: List construction
- **even_odd_game**: Modulo operations

### 2️⃣ Control Flow (7 exercises)
- **amusement_park_ticket**: Age-based conditionals
- **plant_watering_schedule**: String comparison
- **fizz_buzz_lite**: Loop with conditionals
- **elevator_panel**: Range validation
- **rain_streak_counter**: Loop with state tracking
- **simple_dungeon_crawler**: State simulation

### 3️⃣ Methods / Functions (8 exercises)
- **hello_hero**: String formatting
- **vat_calculator**: Tax calculations
- **pizza_planner**: Ceiling division
- **speed_unit_switcher**: Unit conversion
- **grade_average**: Average calculation
- **bank_fee_simulator**: Complex fee calculation
- **tiny_encryption**: Character manipulation

### 4️⃣ Collections & Classes/Objects (17 exercises)
- **shopping_basket**: List sum
- **classroom_scores**: List average
- **mini_rpg**: List processing
- **tip_calculator**: Rounding operations
- **student_records**: Dictionary filtering
- **library**: List membership
- **order_processor**: Conditional processing
- **gradebook**: Class usage and maximum finding
- **matrix_transpose**: 2D list manipulation
- **word_counter**: Dictionary construction
- **file_statistics**: File I/O operations
- **inventory_tracker**: Dictionary updates
- **game_leaderboard**: Sorting operations
- **contact_book**: Tuple to dictionary conversion
- **todo_list**: List filtering
- **student_grades**: Dictionary value processing
- **parking_lot**: Capacity management
- **leaderboard_manager**: List insertion/maintenance

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setting Up the Project

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd python-exercises
   ```

2. **Create a virtual environment:**
   
   **On macOS/Linux:**
   ```bash
   python -m venv venv
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   python -m venv venv
   ```
   
   **On Windows (PowerShell):**
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate
   ```
   
   **On Windows (PowerShell):**
   ```powershell
   venv\Scripts\Activate.ps1
   ```
   
   **Note for Windows PowerShell users:** If you get an execution policy error, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📝 How to Implement an Exercise

### Step 1: Choose an Exercise
Navigate to the `exercises/` directory and pick a file to work on. For example, let's work on `pocket_money_tracker.py`:

```python
# exercises/pocket_money_tracker.py

def calculate_total(monday_amount: int, wednesday_amount: int) -> int:
    """
    Returns monday_amount + wednesday_amount.
    """
    raise NotImplementedError()
```

### Step 2: Implement the Function
Replace `raise NotImplementedError()` with your implementation:

```python
def calculate_total(monday_amount: int, wednesday_amount: int) -> int:
    """
    Returns monday_amount + wednesday_amount.
    """
    return monday_amount + wednesday_amount
```

### Step 3: Run the Tests
Run the specific test for your exercise:

**On macOS/Linux:**
```bash
pytest tests/test_pocket_money_tracker.py -v
```

**On Windows (Command Prompt or PowerShell):**
```cmd
pytest tests\test_pocket_money_tracker.py -v
```

Or run all tests:

**On all platforms:**
```bash
pytest
```

### Step 4: Verify Your Solution
A successful implementation will show:
```
tests/test_pocket_money_tracker.py::test_calculate_total PASSED
```

## 🧪 Running Tests

### Run all tests:
**On all platforms:**
```bash
pytest
```

### Run tests for a specific exercise:
**On macOS/Linux:**
```bash
pytest tests/test_<exercise_name>.py
```

**On Windows (Command Prompt or PowerShell):**
```cmd
pytest tests\test_<exercise_name>.py
```

**Example:**
```bash
# macOS/Linux
pytest tests/test_pocket_money_tracker.py

# Windows
pytest tests\test_pocket_money_tracker.py
```

### Run tests with more detailed output:
```bash
pytest -v
```

### Run a specific test function:
**On macOS/Linux:**
```bash
pytest tests/test_pocket_money_tracker.py::test_calculate_total -v
```

**On Windows:**
```cmd
pytest tests\test_pocket_money_tracker.py::test_calculate_total -v
```

### Windows-Specific Testing Tips

1. **Using Python Module Syntax:**
   If `pytest` command is not recognized, use:
   ```cmd
   python -m pytest tests\test_pocket_money_tracker.py
   ```

2. **File Path Separators:**
   Windows uses backslashes (`\`) instead of forward slashes (`/`) for file paths:
   ```cmd
   # Correct for Windows
   pytest tests\test_pocket_money_tracker.py
   
   # Also works on Windows (pytest handles both)
   pytest tests/test_pocket_money_tracker.py
   ```

3. **Virtual Environment Activation Issues:**
   If you can't activate the virtual environment, try:
   ```cmd
   # From Command Prompt
   venv\Scripts\activate.bat
   
   # From PowerShell (if execution policy allows)
   venv\Scripts\Activate.ps1
   ```

## 📁 Project Structure

```
python-exercises/
├── exercises/                 # Exercise files (implement these!)
│   ├── __init__.py
│   ├── pocket_money_tracker.py
│   ├── cafe_tip_jar.py
│   └── ... (38 more exercises)
├── tests/                     # Test files (do not modify)
│   ├── __init__.py
│   ├── test_pocket_money_tracker.py
│   ├── test_cafe_tip_jar.py
│   └── ... (38 more test files)
├── venv/                      # Virtual environment (auto-generated)
├── requirements.txt           # Python dependencies
├── pytest.ini               # Pytest configuration
└── README.md                 # This file
```

## 💡 Tips for Success

1. **Read the docstrings carefully** - They contain important implementation details
2. **Look at the test cases** - They show expected inputs and outputs
3. **Start with simpler exercises** - Begin with Variables & Primitive Data Types
4. **Test frequently** - Run tests after each small change
5. **Use type hints** - They're provided to help you understand expected types
6. **Don't modify test files** - Only implement functions in the `exercises/` directory

## 🔧 Troubleshooting

### Virtual Environment Issues

**General:**
```bash
# Remove existing venv
rm -rf venv        # macOS/Linux
rmdir /s venv      # Windows Command Prompt

# Create new one
python -m venv venv

# Activate
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

**Windows PowerShell Execution Policy:**
If you get an execution policy error when activating the virtual environment:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again:
```powershell
venv\Scripts\Activate.ps1
```

**Windows Path Issues:**
If pytest is not found after installation:
```cmd
# Use Python module syntax instead
python -m pytest tests\test_pocket_money_tracker.py
```

### Import Errors
Make sure you're running pytest from the project root directory and that your virtual environment is activated.

### Test Failures
- Check that your function signature matches exactly (parameter names, types, return type)
- Verify that your implementation handles the specific test cases
- Look at the assertion error message for clues about what's wrong

### Windows-Specific Issues

1. **Antivirus Software:** Some antivirus programs may interfere with virtual environment creation or script execution. Temporarily disable real-time scanning if you encounter issues.

2. **Long Path Names:** Windows has path length limitations. Keep your project in a shorter directory path if you encounter issues.

3. **Administrator Privileges:** You generally don't need administrator privileges, but if pip installations fail, ensure you're using a virtual environment rather than trying to install system-wide.

## 📖 Learning Path

### Beginner (Start here!)
1. `pocket_money_tracker` - Basic arithmetic
2. `hello_hero` - String formatting
3. `even_odd_game` - Conditionals
4. `shopping_basket` - Lists

### Intermediate
1. `fizz_buzz_lite` - Loops and conditionals
2. `student_records` - Dictionaries
3. `matrix_transpose` - 2D lists
4. `word_counter` - String processing

### Advanced
1. `file_statistics` - File I/O
2. `gradebook` - Classes and objects
3. `leaderboard_manager` - Complex list operations
4. `inventory_tracker` - Dictionary manipulation

## 🎯 Goals

By completing these exercises, you will gain proficiency in:
- Python syntax and basic operations
- Control flow (if/else, loops)
- Data structures (lists, dictionaries, tuples)
- Functions and methods
- Basic object-oriented programming
- File I/O operations
- Problem-solving and algorithmic thinking

Happy coding! 🐍✨ # python-exercises

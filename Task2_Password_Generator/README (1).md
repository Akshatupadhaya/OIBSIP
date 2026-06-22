# Random Password Generator (Python Programming Internship – Task 2)

## Objective
Build a command-line application that generates strong, random passwords
based on user-defined length and character-set preferences.

## Tools Used
- Python 3
- `secrets` module (cryptographically secure randomness)
- `string` module (character set constants)

## Steps Performed
1. Built an input-validation function to confirm the requested password
   length is a whole number between 8 and 64 characters.
2. Let the user choose which character types to include: uppercase
   letters, lowercase letters, digits, and symbols, plus an optional list
   of characters to exclude (e.g. ambiguous characters like `l`, `1`, `O`, `0`).
3. Used Python's `secrets` module instead of `random` to generate
   cryptographically secure random characters, which is the recommended
   approach for anything security-related.
4. Guaranteed the generated password includes at least one character from
   each selected character set, then filled the remaining length randomly
   from the full pool and shuffled the result.
5. Added error handling for cases like an empty character pool or a
   requested length shorter than the number of required character types.
6. Added a loop so the user can generate multiple passwords in one session.

## How to Run
```bash
python3 password_generator.py
```
Follow the on-screen prompts to set the password length and character
types.

## Sample Output
```
Enter desired password length (8-64): 16
Include uppercase letters (A-Z)? [Y/n]: y
Include lowercase letters (a-z)? [Y/n]: y
Include numbers (0-9)? [Y/n]: y
Include symbols (!@#$...)? [Y/n]: y
Characters to exclude (optional, e.g. 'l1O0'):

---------------------------------------------
Generated password: 88g5?9jj^5.IF,Ui
---------------------------------------------
```

## Outcome
A secure, customizable command-line password generator that produces
strong passwords meeting user-specified complexity rules, with input
validation and clear error handling.

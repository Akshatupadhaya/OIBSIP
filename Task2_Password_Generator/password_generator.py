"""
Random Password Generator
A command-line tool that generates a strong random password based on
user-defined length and character set preferences.
"""

import secrets
import string


def get_length():
    """Ask for and validate the desired password length."""
    while True:
        raw_value = input("Enter desired password length (8-64): ").strip()
        if not raw_value.isdigit():
            print("  Please enter a whole number.")
            continue
        length = int(raw_value)
        if length < 8:
            print("  For security, length must be at least 8 characters.")
            continue
        if length > 64:
            print("  Length must be 64 characters or fewer.")
            continue
        return length


def get_yes_no(prompt, default_yes=True):
    """Ask a yes/no question and return True/False."""
    suffix = " [Y/n]: " if default_yes else " [y/N]: "
    while True:
        raw_value = input(prompt + suffix).strip().lower()
        if raw_value == "":
            return default_yes
        if raw_value in ("y", "yes"):
            return True
        if raw_value in ("n", "no"):
            return False
        print("  Please answer y or n.")


def build_character_pool(use_upper, use_lower, use_digits, use_symbols, exclude_chars):
    """Combine the selected character sets into one pool, minus exclusions."""
    pool = ""
    required_sets = []

    if use_upper:
        chars = string.ascii_uppercase
        pool += chars
        required_sets.append(chars)
    if use_lower:
        chars = string.ascii_lowercase
        pool += chars
        required_sets.append(chars)
    if use_digits:
        chars = string.digits
        pool += chars
        required_sets.append(chars)
    if use_symbols:
        chars = "!@#$%^&*()-_=+[]{};:,.<>?/"
        pool += chars
        required_sets.append(chars)

    if exclude_chars:
        pool = "".join(c for c in pool if c not in exclude_chars)
        required_sets = [
            "".join(c for c in s if c not in exclude_chars) for s in required_sets
        ]
        required_sets = [s for s in required_sets if s]

    return pool, required_sets


def generate_password(length, pool, required_sets):
    """Generate a password that includes at least one char from each required set."""
    if not pool:
        raise ValueError("Character pool is empty. Select at least one character type.")
    if length < len(required_sets):
        raise ValueError("Password length is too short to include all required character types.")

    # Guarantee at least one character from each selected set, using a secure RNG.
    password_chars = [secrets.choice(s) for s in required_sets]

    # Fill the rest of the password from the full pool.
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(pool) for _ in range(remaining)]

    # Shuffle so the required characters aren't always at the start.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 45)
    print("        RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    length = get_length()
    use_upper = get_yes_no("Include uppercase letters (A-Z)?")
    use_lower = get_yes_no("Include lowercase letters (a-z)?")
    use_digits = get_yes_no("Include numbers (0-9)?")
    use_symbols = get_yes_no("Include symbols (!@#$...)?")
    exclude_chars = input(
        "Characters to exclude (optional, e.g. 'l1O0'): "
    ).strip()

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("\nNo character types selected. Defaulting to letters + numbers.")
        use_upper = use_lower = use_digits = True

    pool, required_sets = build_character_pool(
        use_upper, use_lower, use_digits, use_symbols, exclude_chars
    )

    try:
        password = generate_password(length, pool, required_sets)
    except ValueError as err:
        print(f"\nError: {err}")
        return

    print("\n" + "-" * 45)
    print(f"Generated password: {password}")
    print("-" * 45)


if __name__ == "__main__":
    while True:
        main()
        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Stay secure.")
            break
        print()

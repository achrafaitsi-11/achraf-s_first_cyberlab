import re
from pathlib import Path 
def check_length(password):

    length = len(password)

    return {
        "length": length,
        "length_8": length >= 8,
        "length_12": length >= 12,
        "length_16": length >= 16,
        "length_20": length >= 20
    }


def check_common_password(password):

    password_file = Path(__file__).parent / "common_passwords.txt"

    try:

        with open(password_file, "r", encoding="utf-8") as file:

            common_passwords = {
                line.strip().lower()
                for line in file
                if line.strip()
            }

        return password.lower() in common_passwords

    except FileNotFoundError:

        return False

def check_common_password(password):

    try:

        with open("common_passwords.txt", "r", encoding="utf-8") as file:

            common_passwords = {
                line.strip().lower()
                for line in file
                if line.strip()
            }

        return password.lower() in common_passwords

    except FileNotFoundError:

        return False


def check_patterns(password):

    password_lower = password.lower()

    sequential_patterns = [
        "1234",
        "2345",
        "3456",
        "4567",
        "5678",
        "6789",
        "abcd",
        "bcde",
        "cdef",
        "defg",
        "efgh",
        "qwer",
        "wert",
        "erty"
    ]

    sequential = any(
        pattern in password_lower
        for pattern in sequential_patterns
    )

    repeated = False

    if len(password) >= 4:

        for i in range(len(password) - 3):

            if len(set(password[i:i + 4])) == 1:
                repeated = True
                break

    # Detect common word + numbers patterns
    normalized = password_lower

    substitutions = {
        "@": "a",
        "4": "a",
        "3": "e",
        "1": "i",
        "0": "o",
        "$": "s",
        "5": "s",
        "7": "t"
    }

    for old, new in substitutions.items():
        normalized = normalized.replace(old, new)

    normalized = re.sub(r"\d+$", "", normalized)

    common_words = [
        "password",
        "admin",
        "welcome",
        "letmein",
        "qwerty",
        "secret",
        "login",
        "football",
        "monkey",
        "dragon",
        "superman",
        "princess"
    ]

    common_pattern = any(
        word in normalized
        for word in common_words
    )

    return {
        "sequential": sequential,
        "repeated": repeated,
        "common_pattern": common_pattern
    }

def check_characters(password):

    return {
        "lowercase": any(char.islower() for char in password),
        "uppercase": any(char.isupper() for char in password),
        "digits": any(char.isdigit() for char in password),
        "special": any(not char.isalnum() for char in password)
    }    

def calculate_score(results):

    score = 0

    length = results["length"]

    # Length
    if length >= 8:
        score += 10

    if length >= 12:
        score += 10

    if length >= 16:
        score += 10

    if length >= 20:
        score += 10

    # Character diversity
    if results["lowercase"]:
        score += 5

    if results["uppercase"]:
        score += 5

    if results["digits"]:
        score += 5

    if results["special"]:
        score += 5

    character_types = sum([
        results["lowercase"],
        results["uppercase"],
        results["digits"],
        results["special"]
    ])

    if character_types >= 3:
        score += 10

    # Penalties
    if results["common"]:
        score -= 40

    if results["sequential"]:
        score -= 15

    if results["repeated"]:
        score -= 15

    if results["common_pattern"]:
        score -=15    
    

    return max(0, min(score, 100))


def get_strength(score, common=False):

    if common:
        return "Weak"

    if score < 20:
        return "Very Weak"

    if score < 40:
        return "Weak"

    if score < 60:
        return "Moderate"

    if score < 80:
        return "Strong"

    return "Very Strong"
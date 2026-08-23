from getpass import getpass

from rules import (
    check_length,
    check_characters,
    check_common_password,
    check_patterns,
    calculate_score,
    get_strength
)


def main():

    print("Password Strength Checker")
    print("-------------------------")

    password = getpass("Enter password: ")

    results = {
        **check_length(password),
        **check_characters(password),
        "common": check_common_password(password),
        **check_patterns(password)
    }

    score = calculate_score(results)

    strength = get_strength(
        score,
        common=results["common"]
    )

    print("\nPassword Analysis")
    print("-----------------")

    print("\nBasic properties:")
    print(f"  Length:             {results['length']}")
    print(f"  Lowercase:          {'Yes' if results['lowercase'] else 'No'}")
    print(f"  Uppercase:          {'Yes' if results['uppercase'] else 'No'}")
    print(f"  Numbers:            {'Yes' if results['digits'] else 'No'}")
    print(f"  Special characters: {'Yes' if results['special'] else 'No'}")

    print("\nSecurity issues:")

    issues_found = False

    if results["common"]:
        print("  [!] Password appears in the common password list.")
        issues_found = True

    if results["sequential"]:
        print("  [!] Contains a predictable sequence.")
        issues_found = True

    if results["repeated"]:
        print("  [!] Contains excessive character repetition.")
        issues_found = True

    if results["common_pattern"]:
        print("  [!] Contains a predictable common-word pattern.")
        issues_found = True

    if not issues_found:
        print("  [OK] No obvious issues detected.")

    print("\nResult:")
    print(f"  Score:    {score}/100")
    print(f"  Strength: {strength}")

    print("\nRecommendations:")

    recommendations_found = False

    if results["length"] < 12:
        print("  - Use a longer password, preferably 12+ characters.")
        recommendations_found = True

    if not results["lowercase"] or not results["uppercase"]:
        print("  - Use a mix of uppercase and lowercase characters.")
        recommendations_found = True

    if not results["digits"]:
        print("  - Consider including numbers.")
        recommendations_found = True

    if not results["special"]:
        print("  - Consider including special characters.")
        recommendations_found = True

    if results["common"]:
        print("  - Avoid passwords found in common-password lists.")
        recommendations_found = True

    if results["sequential"]:
        print("  - Avoid predictable character sequences.")
        recommendations_found = True

    if results["repeated"]:
        print("  - Avoid excessive repetition of the same character.")
        recommendations_found = True

    if results["common_pattern"]:
        print("  - Avoid common words with predictable substitutions or numbers.")
        recommendations_found = True

    if not recommendations_found:
        print("  [OK] No major improvements detected.")


if __name__ == "__main__":
    main()
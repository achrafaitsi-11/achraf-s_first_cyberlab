# Password Strength Checker

A small Python tool that checks a password against a set of basic security rules and gives it a strength score.

The goal is not to determine whether a password is "secure" in an absolute sense, but to identify common weaknesses and explain why a password may be easy to guess.

## What it checks

The checker looks at:

- Password length
- Lowercase and uppercase characters
- Numbers
- Special characters
- Common passwords
- Sequential patterns
- Repeated characters
- Predictable common-word patterns such as `P@ssw0rd123`

The result is a score from 0 to 100 and a strength classification.

## Project structure

```text
password_checker/
├── checker.py
├── rules.py
├── common_passwords.txt
└── README.md

# Regular, um, Expressions
# Problem Set 7

import re
import sys

# Used https://regex101.com/ to check functionality of regular expressions.

def main():
    print(count(input("Text: ")))


def count(s):
    """
    Look for only standalone "um" not within other words, match between zero and infinite times, case-insensitive.

    \b:     Word boundary, matches position where work character is not followed or preceded by another word character (match entire word, not part).
    \w*:    Matches any word character zero or more times.
    um:     Character(s) that need to be matched.
    \w*:    Matches any word character zero or more times.
    \b:     Word boundary, match entire word, not part.

    re.I or re.IGNORECASE makes the regex case insensitive.
    """


    um_list = re.findall(r"\b\W*um\W*\b",s, re.IGNORECASE)
    return len(um_list)


if __name__ == "__main__":
    main()
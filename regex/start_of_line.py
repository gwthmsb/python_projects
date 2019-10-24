"""
Given a sentence,  write a RegEx to match the following criteria:

The first character must be the letter H or h.
The second character must be the letter I or i.
The third character must be a single space (i.e.: \s).
The fourth character must not be the letter D or d.
Given  lines of sentences as input, print each sentence matching your RegEx on a new line.

"""

import re

# (?...) is called extension notation

def main():
    reg = "^[Hh][iI]\s(?![Dd])"

    n = int(raw_input())

    for i in range(0, n):
        input_string = raw_input()
        if re.match(reg, input_string):
            print(input_string)


if __name__ == "__main__":
    main()


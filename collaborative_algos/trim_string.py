# Given a string that may have extra spaces at the start and the end,
# return a new string that has the extra spaces at the start and the end trimmed (removed)
# do not remove any other spaces.

str1 = "   hello world     "
expected1 = "hello world"

str2 = "    the   quick brown     fox     "
expected2 = "the quick brown fox"

# Trims any leading or trailing white space from the given str.
# - Time: O(?).
# - Space: O(?).
# @param {string} str
# @returns {string} The given string with any leading or trailing white space
# stripped.

# Using builtin function

import re

def trim(string_in):
    return string_in.strip()


def trim_functional(input_str):
    # remove duplicate sequences of spaces
    string_in = re.sub(r'\s+', ' ', input_str)

    chars_out = []

    for x in range(0, len(string_in)):
        if string_in[x].isalpha():
            chars_out.append(string_in[x])
        elif x < len(string_in) - 1:
            if string_in[x].isspace() and string_in[x + 1].isalpha() and string_in[x - 1].isalpha():
                chars_out.append(string_in[x])

    # chars_out = [string_in[x] for x in range(len(string_in)) if string_in[x].isalpha() or (
    #             x > 0 and x < len(string_in) - 1 and string_in[x].isspace() and string_in[x + 1].isalpha() and
    #             string_in[x - 1].isalpha())]

    return ''.join(chars_out)


if __name__ == "__main__":
    print(f'[{trim_functional(str1)}]')
    print(f'[{trim_functional(str2)}]')

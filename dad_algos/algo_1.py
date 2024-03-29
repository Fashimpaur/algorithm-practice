# Given a string that may have extra spaces at the start and the end,
# return a new string that has the extra spaces at the start and the end trimmed (removed)
# do not remove any other spaces.

str1 = "   hello world     "
expected1 = "hello world"

# Trims any leading or trailing white space from the given str.
# - Time: O(?).
# - Space: O(?).
# @param {string} str
# @returns {string} The given string with any leading or trailing white space
# stripped.

# Using builtin function
def trim(string_in):
    return string_in.strip()


def trim_functional(string_in):
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




#     An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#     typically using all the original letters exactly once.

#     Is there a quick way to determine if they aren't an anagram before spending more time?

#     Given two strings
#     return whether or not they are anagrams


strA1 = "yes"
strB1 = "eys"
expected2 = True

strA2 = "yes"
strB2 = "eYs"
expected3 = True

strA3 = "no"
strB3 = "noo"
expected4 = False

strA4 = "silent"
strB4 = "listen"
expected5 = True

strA5 = "yes"
strB5 = "eee"

strA6 = "eee"
strB6 = "sss"

#  * Determines whether s1 and s2 are anagrams of each other.
#  * Anagrams have all the same letters but in different orders.
#  * - Time: O(?).
#  * - Space: O(?).
#  * @param {string} s1
#  * @param {string} s2
#  * @returns {boolean} Whether s1 and s2 are anagrams.


def is_anagram(str1, str2):
    # Check if lengths are not equal; return False
    if len(str1) != len(str2):
        return False

    # Declare variables to hold str1 and str2 as lowercase and status
    map_dict = {}
    first = str1.lower()
    second = str2.lower()
    status = True

    # Loop through second
    for char in second:
        # Check if first does contain the character
        if char not in first:
            status = False
            break
            # If true; add character to hash map
        if char in map_dict:
            map_dict[char] += 1
        else:
            map_dict[char] = 1

    for value in map_dict.values():
        if value > 1:
            status = False
            break

    return status



if __name__ == "__main__":
    print("It was...")
    print(str1)
    print("It is...")
    print(f'[{trim_functional(str1)}]')

    # print(is_anagram(strA1, strB1))
    # print(is_anagram(strA2, strB2))
    # print(is_anagram(strA3, strB3))
    # print(is_anagram(strA4, strB4))
    # print(is_anagram(strA5, strB5))
    # print(is_anagram(strA6, strB6))
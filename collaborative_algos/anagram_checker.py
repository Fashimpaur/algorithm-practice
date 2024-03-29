#     An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#     typically using all the original letters exactly once.

#     Is there a quick way to determine if they aren't an anagram before spending more time?

#     Given two strings
#     return whether they are anagrams or not


strA1 = "yes"
strB1 = "eys"
anag_expected1 = True

strA2 = "yes"
strB2 = "eYs"
anag_expected2 = True

strA3 = "no"
strB3 = "noo"
anag_expected3 = False

strA4 = "silent"
strB4 = "listen"
anag_expected4 = True

strA5 = "yes"
strB5 = "eee"
anag_expected5 = False

strA6 = "eee"
strB6 = "sss"
anag_expected6 = False

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
    print(is_anagram(strA1, strB1))
    print(is_anagram(strA2, strB2))
    print(is_anagram(strA3, strB3))
    print(is_anagram(strA4, strB4))
    print(is_anagram(strA5, strB5))
    print(is_anagram(strA6, strB6))
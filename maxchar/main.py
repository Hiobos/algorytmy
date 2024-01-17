from collections import Counter

# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
#maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

def maxChar(strnum):
    char_count = {}

    for char in strnum:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    maxChar = max(char_count, key=char_count.get)
    return maxChar
/**
Check whether two strings contain same characters in same order
Last Updated : 19 Dec, 2022
Given two strings s1 and s2, the task is to find whether the two strings contain the same characters that occur in the same order. 
For example string “Geeks” and string “Geks” contain the same characters in same order.

Examples: 


Input: s1 = “Geeks”, s2 = “Geks” 
Output: Yes


Input: s1 = “Arnab”, s2 = “Andrew” 
Output: No 

**/


def remove_adjacent_repeating_chars(s):
    # Convert string to lowercase for case insensitivity (optional)
    s = s.lower()
    result = [s[0]]  # Initialize result with the first character
    
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:  # Add only if different from previous char
            result.append(s[i])
    
    return "".join(result)

def is_subsequence(small, large):
    """
    Checks if 'small' is a subsequence of 'large'
    """
    it = iter(large)
    return all(char in it for char in small)

def find_match(str1, str2):
    if is_subsequence(str1, str2) or is_subsequence(str2, str1):
        print("Match")
    else:
        print("Don't Match")

if __name__ == "__main__":
    str1 = "Geksr"
    str2 = "Geerks"
    str1 = remove_adjacent_repeating_chars(str1)  # Gerks
    str2 = remove_adjacent_repeating_chars(str2)  # Geks
    find_match(str1, str2)

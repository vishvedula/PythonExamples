/*Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.
Check the sample test case for reference.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Problem Constraints
1 <= |A| <= 106
Input Format
The first argument is a string A.
Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example Input
Input 1:
"A man, a plan, a canal: Panama"
Input 2:
"race a car"

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
The input string after ignoring spaces, and all special characters is "AmanaplanacanalPanama" 
which is a palindrome after ignoring the case.
Explanation 2:
The input string after ignoring spaces, and all special characters is "raceacar" which is not a palindrome*/

import re

def is_palindrome(s):
  """Checks if a given string is a palindrome after removing non-alphanumeric characters.

  Args:
    s: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  # Remove non-alphanumeric characters and convert to lowercase
  cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

  # Check if the cleaned string is equal to its reverse
  return cleaned_string == cleaned_string[::-1]

# Example usage:
string = "race a car"

if is_palindrome(string):
  print("It's a palindrome!")
else:
  print("It's not a palindrome.")

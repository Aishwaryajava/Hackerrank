# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# I thought of using a predefined function to check the reverse string with the original string.

# # Approach
# <!-- Describe your approach to solving the problem. -->
# 1.convert the integer to the string.
# 2.Reverse the string using the predefined function ‘ ‘.join(reversed(string))
# 3.Check if the converted string and reversed string are the same.

# # Complexity
# - Time complexity:
# O(n)

# - Space complexity:
# O(n)

#Code 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converting integer to string 
        converted_x = str(x)
        # Using predefined function to reverse to string print(x)
        rev = ''.join(reversed(converted_x))

        # Checking if both string are equal or not
        if (converted_x == rev):
            return True
        return False
#Main Function
x = 121

# The function isPalindrome is a method of the Solution class. Therefore, when you call it, you should create an instance of the Solution class and then call the method on that instance.
solution_instance = Solution()
ans = solution_instance.isPalindrome(x)
 
if (ans):
    print("Yes")
else:
    print("No")

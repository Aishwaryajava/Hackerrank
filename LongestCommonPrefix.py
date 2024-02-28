class Solution:
    # Function to find the common prefix between two strings
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # If the list of strings is empty
        if len(strs) == 0:
            return ""

        # If the list contains only one string, that string is the whole list of strings
        if len(strs) == 1:
            return strs[0]

        # Setting the prefix as empty to store the value
        prefix = ""

        # Find the shortest string in the list
        shortest = min(strs, key=len)

        # Iterate over the characters to find the length of the prefix
        for i in range(len(shortest)):
            char = shortest[i]
            # Compare the shortest with the characters in other strings
            for string in strs:
                if string[i] != char:
                    return prefix
            # If the characters match, append it to the prefix
            prefix += char

        return prefix

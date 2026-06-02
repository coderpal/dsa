class Solution:
    def reverseWords(self, s: str) -> str:

        # use .split() ti remove all extra spaces between words
        # converts string into list of words
        words = s.split()

        # initialize start and end pointers
        left = 0
        right = len(words) - 1

        # use two-pointer swap logic
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # join the reversed words back and add a single space
        return " ".join(words)
        
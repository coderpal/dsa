class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # initialize the empty dictionary
        freq = {}

        # count all the char frequency in s
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # scan s again and return the first index where count = 1
        for index, char in enumerate(s):  # enumerate gives both index and value
            if freq[char] == 1:
                return index

        return -1
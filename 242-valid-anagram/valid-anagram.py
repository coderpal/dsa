class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Sanity Check: if lengths are not same, return False
        if len(s) != len(t):
            return False

        # initialise empty dictionary
        count_s = {}
        count_t = {}

        # map frequency, use zip(s,t)
        for char_s, char_t in zip(s,t):
            count_s[char_s] = count_s.get(char_s, 0) + 1
            count_t[char_t] = count_t.get(char_t, 0) + 1

        return count_s == count_t
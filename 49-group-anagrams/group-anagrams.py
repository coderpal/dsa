class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # initialize empty dict
        groups = {}

        for word in strs:
            # sorted for ascending order of each word in strs
            # "". join() to put back all the characters back to str
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # initialize empty dictionary
        freq = {}
        n = len(nums)

        # map the frequency
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

            # now count
            # if count is greater than half the length of array, return it
            if freq[x] > n//2:
                return x
        
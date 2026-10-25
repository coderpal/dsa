class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # empty dictionary to store already seen numbers and its indices
        seen = {}

        # check if the number and its index is already there in the seen dictionary
        for i, n in enumerate(nums):
            # calculate difference between target and the number
            diff = target - n

            # check if difference already in seen dict
            if diff in seen:
                # return difference and its index
                return [seen[diff], i]

            # else, add the element in the seen dictionary
            seen[n] = i

        return []
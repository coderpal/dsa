class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # initialise the empty dictionary where num = key & index = value
        seen = {}

        # loop from left to right, using enumerate to have the key-value pair
        for index, num in enumerate(nums):

            # complement logic, the core logic
            complement = target - num

            # if statement if complement is in the seen dictionary
            if complement in seen:

                # return the index of the complement in the seen and current position index
                return [seen[complement], index]

            # if complement not in seen, save the key-value (nums-index) pair in the dict for further lookup
            seen[num] = index
        
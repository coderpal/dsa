class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        # initialize tracker
        # even at index 0 and odd at index 1
        even = 0
        odd = 1
        n = len(nums)

        # loop till the array is exhausted
        while even < n and odd < n:

            # if even index holds even number, skip it
            if nums[even] % 2 == 0:
                even += 2
            # if odd index holds odd number, skip it
            elif nums[odd] % 2 != 0:
                odd += 2
            # if misplaced, swap using two-pointer swap logic
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2

        return nums
        
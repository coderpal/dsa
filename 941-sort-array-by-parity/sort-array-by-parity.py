class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # initialize start and end pointers
        left = 0
        right = len(nums) - 1

        while left < right:

            # if left is already even, skip
            if nums[left] % 2 == 0:
                left += 1
            # if right is already odd, skip
            elif nums[right] % 2 != 0:
                right -= 1
            # two-pointer swap logic
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
        
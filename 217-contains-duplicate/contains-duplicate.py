class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # initialize set. (hash set)
        seen = set()

        # check if element in nums are already in set seen
        for num in nums:
            if num in seen:
                # return true if the nums are already in set seen
                return True
            else:
                # if not in set seen, add them
                seen.add(num)

        # return false if all elements are distinct at the end of the loop
        return False
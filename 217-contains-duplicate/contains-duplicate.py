class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # inititialize empty set
        seen = set()

        for x in nums:
            # check if the value is already in the set
            # if True, then its a duplicate
            if x in seen:
                return True

            # add other element in set for loop to continue
            seen.add(x)

        # if all elements are distinct
        return False
        
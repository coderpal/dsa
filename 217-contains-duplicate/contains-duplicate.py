class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # initialize empty set
        seen = set()

        # for loop to loop through the array
        for num in nums:

            # check if the element exists in the set
            if num in seen:

                # if exists, then it is duplicate
                # return True
                return True

            # if not exists in seen, add that element in set
            # will be useful till the loop ends
            seen.add(num)

        # if no duplicate exists finally at the end of loop, return False
        return False
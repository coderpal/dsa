class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # initialize empty dict
        last_seen = {}

        for i, x in enumerate(nums):
            if x in last_seen:
                # check if distance between indices
                if i - last_seen[x] <= k:
                    return True
            # store latest index of x
            last_seen[x] = i

        return False
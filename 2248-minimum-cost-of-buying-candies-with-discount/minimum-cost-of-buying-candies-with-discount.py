class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        # sort candies from most expensive to cheapest
        cost.sort(reverse = True)
        totalCost = 0

        # loop through the list with step 3
        for i in range(len(cost)):

            # skip every 3rd candy as it is free
            if (i + 1) % 3 == 0:
                continue
            totalCost += cost[i]

        return totalCost
        
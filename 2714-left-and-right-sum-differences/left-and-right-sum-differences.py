class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Initialize leftSum as 0 and rightSum as the total sum of the array
        left_sum = 0
        right_sum = sum(nums)
        
        answer = []
        
        for num in nums:
            # Subtract current element from right_sum because rightSum[i] 
            # is the sum of elements strictly to the right of i
            right_sum -= num
            
            # Calculate the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Add current element to left_sum for the next iteration
            left_sum += num
            
        return answer
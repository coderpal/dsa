from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(num_str: str) -> int:
            n = len(num_str)
            
            # DP State: (index, last_digit, second_last_digit, is_tight, has_started)
            @lru_cache(None)
            def dp(idx: int, prev1: int, prev2: int, is_tight: bool, is_started: bool):
                # Base Case: If we reach the end, we've successfully formed 1 valid number
                if idx == n:
                    return (1 if is_started else 0), 0
                
                # Determine upper bound for the current digit
                limit = int(num_str[idx]) if is_tight else 9
                
                total_count = 0
                total_waviness = 0
                
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    
                    if not is_started:
                        if d == 0:
                            # Skip leading zeros
                            c, w = dp(idx + 1, -1, -1, next_tight, False)
                        else:
                            # First actual digit placed
                            c, w = dp(idx + 1, d, -1, next_tight, True)
                    else:
                        if prev2 == -1:
                            # Second digit placed (not enough history for waviness yet)
                            c, w = dp(idx + 1, d, prev1, next_tight, True)
                        else:
                            # 3+ digits placed. Evaluate if 'prev1' is a peak or a valley
                            is_peak = (prev2 < prev1) and (prev1 > d)
                            is_valley = (prev2 > prev1) and (prev1 < d)
                            waviness_delta = 1 if (is_peak or is_valley) else 0
                            
                            c, w = dp(idx + 1, d, prev1, next_tight, True)
                            
                            # Standard Digit DP math: The current choice adds its localized 
                            # waviness contribution multiplied by how many valid suffixes it can make.
                            w += waviness_delta * c
                    
                    total_count += c
                    total_waviness += w
                    
                return total_count, total_waviness

            # We only care about the total waviness accumulator (index 1 of the returned tuple)
            return dp(0, -1, -1, True, False)[1]

        # Standard range query logic: f(num2) - f(num1 - 1)
        return solve(str(num2)) - solve(str(num1 - 1))
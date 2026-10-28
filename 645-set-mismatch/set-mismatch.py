class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Expected sums for numbers from 1 to n
        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
        
        # Actual sums from the given array
        actual_sum = sum(nums)
        actual_sq_sum = sum(x * x for x in nums)
        
        # Let x be the duplicate and y be the missing number
        # x - y = actual_sum - expected_sum
        diff = actual_sum - expected_sum
        
        # x^2 - y^2 = actual_sq_sum - expected_sq_sum
        # (x - y)(x + y) = actual_sq_sum - expected_sq_sum
        sq_diff = actual_sq_sum - expected_sq_sum
        
        # x + y = sq_diff / diff
        sum_xy = sq_diff // diff
        
        # Solve system of linear equations:
        # 2x = diff + sum_xy
        duplicate = (diff + sum_xy) // 2
        missing = sum_xy - duplicate
        
        return [duplicate, missing]
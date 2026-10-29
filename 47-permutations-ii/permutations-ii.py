class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                # Skip if already used
                if used[i]:
                    continue
                
                # Skip duplicates: if current element is same as previous, 
                # and previous was not used in this branch, skip to avoid duplicate permutations.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                path.pop()
                used[i] = False
                
        backtrack([])
        return res
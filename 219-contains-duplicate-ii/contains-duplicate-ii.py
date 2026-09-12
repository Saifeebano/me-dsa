class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i, num in enumerate(nums):
            # Agar number pehle se window mein hai, toh Duplicate found!
            if num in seen:
                return True
            
            # Current number ko set mein add karo
            seen.add(num)
            
            # Agar window ka size k se bada ho jaye, toh sabse purane number ko hata do
            if len(seen) > k:
                seen.remove(nums[i - k])
                
        return False
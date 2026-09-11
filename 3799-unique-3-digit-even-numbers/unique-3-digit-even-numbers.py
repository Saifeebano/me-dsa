from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        digits_count = Counter(digits)
        result = 0
        
        # Iterate through all 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            num_count = Counter([d1, d2, d3])
            
            # Check if all required digits are available in digits_count
            if all(digits_count[d] >= count for d, count in num_count.items()):
                result += 1
                
        return result
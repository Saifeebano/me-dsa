class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return[]

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }    
        result = []
        def backtrack(index, current_string):
            if len(current_string) == len(digits):
                result.append(current_string)
                return

            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                backtrack(index + 1, current_string + letter)

        backtrack(0, "")
        return result    
                


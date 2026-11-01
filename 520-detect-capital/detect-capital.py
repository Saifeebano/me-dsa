class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all letters are uppercase, all are lowercase, or only the first letter is capitalized
        return word.isupper() or word.islower() or word.istitle()
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary to hold the grouped anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to form the key
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())
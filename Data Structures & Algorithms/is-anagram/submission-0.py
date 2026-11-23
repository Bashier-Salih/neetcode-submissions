class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        print(freq)
        
        for c in t:
            if c in freq:
                freq[c] -= 1
        
        for value in freq.values():
            if value != 0:
                return False

        return True
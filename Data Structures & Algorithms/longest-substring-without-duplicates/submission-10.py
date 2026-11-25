class Solution:
    """
    Understand:
    Input: A string
    Output: an int representing the longest substring withough repeating chars
    Edge Cases: string of length 0
    
    Plan:
    create a l,r pointers for a window
    create an empty set
    longest = 0


    while r < len(s):
        if s[r] not in set:
            add s[r] into set
            increment r
        else:
            longest = max(longest, r - l + 1)
            l = r
    
    return longest
        


    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        longest = 0

        for r in range(len(s)):
            #print(chars)
            if s[r] not in chars:
                chars.add(s[r])
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
            longest = max(longest, r - l + 1)
            
        
        return longest
        
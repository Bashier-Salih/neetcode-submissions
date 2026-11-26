class Solution:
    """
    Understand:
    Input: two strings
    Output: a single substring of s
    Edge cases: if they are the same, return s
                if len(s) < len(t):
                    return ""
    
    Plan:
    tackle edge cases
    freq_t = {}
    result = ""
    l = 0

    for c in t:
        freq_t[c] = freq_t.get(c, 0) + 1
    
    for r in range(len(s)):
        if nums[r] in freq_t:
            result += nums[r]
            freq_t[nums[r]] -= 1
        else:
            l = r
            result = ""
    """
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t) :
            return ""
        
        countT, window = {}, {}
        l = 0
        res, resLength = [-1,-1], float("inf")

        for c in t:
            countT[c] = countT.get(c,0) + 1
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            current = s[r]
            window[current] = window.get(current, 0) + 1

            if current in countT and window[current] == countT[current]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLength:
                    resLength = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                    
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res[0], res[1]
        print(res)
        if resLength != float("inf"):
            return s[l: r + 1]
        return ""
                

                


        
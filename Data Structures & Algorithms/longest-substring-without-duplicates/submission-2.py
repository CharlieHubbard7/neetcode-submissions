class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        window = dict()
        maxLength = 0
        for i, ch in enumerate(s):
            if ((ch not in window) or (window[ch] < lo)):
                window[ch] = i
                maxLength = max(maxLength, i - lo + 1)
            else:
                lo = window[ch] + 1
                window[ch] = i
        return maxLength
            

            

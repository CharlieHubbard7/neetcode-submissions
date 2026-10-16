class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lo = 0
        s1len = len(s1)
        for i in range(len(s2) - s1len + 1):
            current = s2[i:i+s1len]
            if self.isPermutation(s1, current):
                return True
        return False


    def isPermutation(self, s1, s2):
        s1map = dict()
        s2map = dict()
        len1, len2 = len(s1), len(s2)
        if len1 != len2: return False
        for i in range(len(s1)):
            if s1[i] not in s1map: s1map[s1[i]] = 1
            else: s1map[s1[i]] += 1
            if s2[i] not in s2map: s2map[s2[i]] = 1
            else: s2map[s2[i]] += 1
        
        return s1map == s2map

print(Solution().isPermutation('hi', 'ih'))
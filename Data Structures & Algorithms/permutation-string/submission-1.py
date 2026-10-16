class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lo = 0
        s1len = len(s1)
        s1map = dict()
        for i in range(len(s1)):
            if s1[i] not in s1map: s1map[s1[i]] = 1
            else: s1map[s1[i]] += 1


        
        for i in range(len(s2) - s1len + 1):
            current = s2[i:i+s1len]
            if self.isPermutation(s1map, current):
                return True
        return False


    def isPermutation(self, s1map, s2):
        s2map = dict()
        for i in range(len(s2)):
            if s2[i] not in s2map: s2map[s2[i]] = 1
            else: s2map[s2[i]] += 1
        
        return s1map == s2map

print(Solution().isPermutation('hi', 'ih'))
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""

    def isPalindrome(self, words):
        length = len(words)
        midpoint = length//2
        for i in range(midpoint):
            left = words[i]
            right = words[-1-i]
            if left != right:
                return False
        return True
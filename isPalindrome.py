class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return self.func(s, 0, len(s)-1)

    def func(self,s,l,r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return self.func(s,l+1,r-1)
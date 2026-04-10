class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        
        count = 0
        n = len(s)
        for i in range(n//2):
            if s[i] == s[n-i-1]:
                count+=1
        
        if count == n//2:
            return True
        else:
            return False   
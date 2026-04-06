class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count =0
        if len(s) == len(t):
            for i in range(len(s)):
                for j in range(len(t)):
                    if s[i] == t[j]:
                        count+=1
                        t= t[:j] + t[j+1:]
                        break 
        
        if count == len(s):
            return True
        else:
            return False
                
        
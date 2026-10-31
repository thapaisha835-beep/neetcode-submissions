class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d1,d2 = {},{}
            for i in range(len(s)):
                try:
                    d1[s[i]] += 1
                except:
                    d1[s[i]] = 1
                try:
                    d2[t[i]] += 1
                except:
                    d2[t[i]] = 1
            if d1 == d2:
                return True
        return False
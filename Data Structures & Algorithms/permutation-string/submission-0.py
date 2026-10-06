class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s11 = sorted(s1)
        lgt = len(s1)
        for i in range(len(s2)- lgt + 1):
            if sorted(s2[i:i+lgt]) == s11:
                return True
        return False
        
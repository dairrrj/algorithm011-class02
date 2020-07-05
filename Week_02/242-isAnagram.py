class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        if (len(s) != len(t)) or (set(s) != set(t)):
            return False
        d={}
        for item in s:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for item in t:
            if item in d:
                d[item] -= 1
            else:
                return False
        for item in d:
            if d[item] != 0:
                result = False
                break

        return result
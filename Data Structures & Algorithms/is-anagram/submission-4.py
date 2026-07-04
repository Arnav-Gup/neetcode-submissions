class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        if len(t) != len(s):
            return False

        for x in s:
            maps[x] = maps.get(x, 0)+1

        for x in t:
            if x not in maps:
                return False
            maps[x] -= 1
            if maps[x]<=0:
                del maps[x]

        return True
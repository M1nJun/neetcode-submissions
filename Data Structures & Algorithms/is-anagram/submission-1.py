class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I need to save unique char and counts of each
        charMap = {}

        for x in s:
            charMap[x] = charMap.get(x, 0)+1
        
        for x in t:
            # if charMap[x] doesn't exist or already at 0, we can return False
            if charMap.get(x, 0) == 0:
                return False
            charMap[x]-=1
        
        for x in charMap.values():
            if x != 0:
                return False
        
        return True
        
        # if all the values left on the map is 0, we can return true
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I need to save unique char and counts of each
        charMap = {}

        for x in s:
            if x in charMap:
                charMap[x]+=1
            else:
                # I think there was a get function that was useful
                # that either gets the current value if the key exists,
                # or create one and assign the value that I hand it as a param
                # like charMap.get(x, 0)
                charMap[x] = 1
        
        for x in t:
            if x not in charMap:
                return False
            charMap[x]-=1
        
        for x in charMap.values():
            if x != 0:
                return False
        
        return True
        
        # if all the values left on the map is 0, we can return true
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for x in nums:
            if x not in dup:
                dup.add(x)
            else:
                return True
        return False
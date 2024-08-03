class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for x in target:
            if x in arr:
                arr.remove(x)
            else:
                return False
        return True

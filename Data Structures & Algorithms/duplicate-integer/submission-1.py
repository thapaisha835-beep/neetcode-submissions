class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            try:
                d[i] += 1
                return True
            except:
                d[i] = 1      
        
        return False

        
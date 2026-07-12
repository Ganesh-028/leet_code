class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = 0
        
        for n in nums:
            if n in seen:
                duplicate = n
            seen.add(n)
        
        missing = 0
        
        for i in range(1, len(nums)+1):
            if i not in seen:
                missing = i
        
        return [duplicate, missing]

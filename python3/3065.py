class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op = 0
        for i in nums:
            if i < k:
                op += 1
        return op
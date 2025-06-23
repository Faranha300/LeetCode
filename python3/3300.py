class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in nums:
            num_int = 0
            for j in str(i):
                num_int += int(j)
            nums[nums.index(i)] = num_int
        nums.sort()
        return nums[0]
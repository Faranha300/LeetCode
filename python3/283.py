class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(count):
            index = nums.index(0)
            nums.pop(index)
            nums.append(0)
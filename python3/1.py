class Solution(object):
    def twoSum(self, nums, target):
        countI = 0
        countJ = 0
        for i in nums:
            for j in nums:
                if i + j == target and countI != countJ:
                    return [countI, countJ]
                countJ += 1
            countJ = 0
            countI += 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for a in range(0, length):
            for b in range(0, length):
                if nums[a] + nums[b] == target and a != b:
                    return [a, b]

        return [1,1]
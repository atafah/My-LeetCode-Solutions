class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation_arr = []
        for n in nums:
            permutation_arr.append(nums[n])

        return permutation_arr
        
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(n)
        ans *= 2
        return ans
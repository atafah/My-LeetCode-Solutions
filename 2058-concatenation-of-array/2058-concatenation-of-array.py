class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        ans = []
        for n in nums:
            a.append(n)
        ans.extend(a)
        ans.extend(a)
        return ans
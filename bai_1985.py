#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=[]
        for i in nums:
            a.append(int(i))
        b=sorted(a,reverse=True)
        return str(b[k-1])
# @lc code=end


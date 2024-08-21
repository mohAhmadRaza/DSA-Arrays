Method 1:

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]

        for i in range(1, len(nums)):
            ans.append(ans[-1]+nums[i])
        
        return ans

Method 2:

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(nums[0)

        for i in range(1, len(nums)):
            ans.append(ans[i-1]+nums[i])
        
        return ans

Method 3:

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]
            ans.append(sums)
        
        return ans

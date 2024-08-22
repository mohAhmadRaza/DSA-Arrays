class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # Finding Distinct elements in the list : nums
        num = list(set(nums))
        
        # Now sorting the list in descending order
        num.sort(reverse=True)
        
        # If length is less than expected, return maximm element
        if len(num) < 3:
            return max(num)
        
        # Return third element
        return num[2]

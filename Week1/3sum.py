# Link -> https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                _sum = a + b + c
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    result.append([a,b,c])
                    left += 1
                    while left < right and nums[left] == b:
                        left += 1
                    
                    right -= 1
                    while left < right and nums[right] == c:
                        right -= 1
        return result
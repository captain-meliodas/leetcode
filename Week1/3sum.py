# Link -> https://leetcode.com/problems/3sum/

# input = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort if sum is less than 0 we move left+1 and if greater than 0 we move from right-1[-4,-1,-1,0,1,2]
        n = len(nums)
        result = []
        for i,a in enumerate(nums): # get index and value from array list
            if i>0 and a == nums[i-1]: #ignore if we get same number on continuous move
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
                    result.append([a,b,c]) #if sum is 0 append values
                    left += 1
                    while left < right and nums[left] == b: #skip all left if left+1 is equal to left till we reaches right
                        left += 1
                    
                    right -= 1
                    while left < right and nums[right] == c: #skip all right if right-1 is equal to right till we reaches left
                        right -= 1
        return result
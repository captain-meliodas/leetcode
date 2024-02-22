#Link -> https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target - n #get the difference
            if diff in prevMap: #check if difference is present in map keys
                return [prevMap[diff],i] #return index of diff and current index
            prevMap[n] = i #otherwise add diff as key and value as index
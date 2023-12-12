#Link -> https://leetcode.com/problems/first-bad-version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high)//2
        badVersion = 1

        while low <= high:
            if isBadVersion(mid):
                badVersion = mid
                high = mid-1
                mid = (low+high)//2
            else:
                low = mid+1
                mid = (low+high)//2
        
        return badVersion

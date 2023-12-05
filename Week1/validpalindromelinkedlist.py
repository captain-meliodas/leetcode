#Link -> https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _len = 0
        temp = head
        while temp:
            _len += 1
            temp = temp.next
        mid_idx = _len // 2 
        if mid_idx == 0:
            return True
        temp = head
        s1 = s2 = ""
        i = 1
        while temp:
            if i <= mid_idx:
                s1 = f"{s1}{temp.val}"
            else:
                s2 = f"{temp.val}{s2}"
            temp = temp.next
            i += 1

        if _len%2 != 0:
            s1 = f"{s1}{s2[-1]}"
            
        return s1 == s2
        
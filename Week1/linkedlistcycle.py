#Link -> https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Solution 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head

        while temp:
            if temp.val == 'v':
                return True
            temp.val = 'v'
            temp = temp.next
        
        return False


#Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowp = fastp = head

        while fastp and fastp.next:
            fastp = fastp.next.next
            slowp = slowp.next
            if fastp == slowp:
                return True
        
        return False

        
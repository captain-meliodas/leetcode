#Link-> https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None

        while head:
            currentNode = head
            head = head.next
            currentNode.next = prevNode
            prevNode = currentNode
        
        return prevNode
            
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        po1 = head
        po2 = head
        
        while po2 != None and po2.next != None:
            po1=po1.next
            po2=po2.next.next
            if po1==po2:
                return True
        return False
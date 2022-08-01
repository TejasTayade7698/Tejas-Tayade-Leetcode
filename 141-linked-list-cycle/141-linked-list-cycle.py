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
        self.head=head
        s=set()
        temp=self.head
        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)
                temp=temp.next
            
        return False
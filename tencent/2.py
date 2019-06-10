# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l3=None
        cache=0
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1_value=0
            else:
                l1_value=l1.val
            if l2 is None:
                l2_value=0
            else:
                l2_value=l2.val
            value=l1_value+l2_value+cache
            if value>9:
                cache=1
                value=value-10
            else:
                cache=0
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
            new_node=ListNode(value)
            if l3 is None:
                l3=new_node
                head=l3
            else:
                l3.next=new_node
                l3=l3.next
        if cache!=0:
            new_node=ListNode(cache)
            l3.next=new_node
        return head
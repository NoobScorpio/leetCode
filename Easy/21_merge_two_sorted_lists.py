
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        tail = head

        if None in (l1,l2):
            return l1 or l2
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return head.next




# MERGE TWO NODES
l1 = ListNode( val= 1, next= ListNode(val= 2, next= ListNode(val= 4, next= None)))
l2 = ListNode( val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None)))
print(str(ListNode.mergeTwoLists(l1,l2)))


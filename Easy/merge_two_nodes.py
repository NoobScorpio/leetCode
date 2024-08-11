
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    h1 =list1
    h2 =list2
    l = []
    while h1:
        l.append(h1.val)
        print(l)
        h1=h1.next
        
    print("BEFORE LOOP 2: " + str(l))
    while h2:
        l.append(h2.val)
        h2 = h2.next
        
    print("After LOOP 2: " + str(l))
    l.sort()
    print("After SORT" + str(l))
        
    i = 1
    my_list = ListNode(l[0],None)
        
    while i < len(l):
        my_list.next = ListNode(l[i],None)
        i +=1
        
    return my_list




# MERGE TWO NODES
l1 = ListNode( val= 1, next= ListNode(val= 2, next= ListNode(val= 4, next= None)))
l2 = ListNode( val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None)))
print(str(mergeTwoLists(l1,l2)))


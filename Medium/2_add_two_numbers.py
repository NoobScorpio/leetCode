# NEED TO OPTIMIZE THE CODE

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print(l1)
        s1 = ""
        s2 = ""
        curr = l1
        while curr is not None:
            s1 += str(curr.val)
            curr = curr.next
        print(s1)
        s1r =""
        i = len(s1)-1
        while i >= 0:
            s1r += s1[i]
            i-=1
        print(s1r)
        curr = l2
        while curr is not None:
            s2 += str(curr.val)
            curr = curr.next
        print(s2)
        s2r =""
        i = len(s2)-1
        while i >= 0:
            s2r += s2[i]
            i-=1
        print(s2r)
        ans = int(s1r) + int(s2r)

        ans = str(ans)
        print(ans)
        ansr =""
        i = len(ans)-1
        while i >= 0:
            ansr += ans[i]
            i-=1
        i = 0
        print(ansr)
        head = ListNode(val=int(ansr[i]),next = None)
        ans = head
        i = 1
        while i <  len(ansr):
            print(ans)
            ans.next = ListNode(val=int(ansr[i]),next = None)
            ans = ans.next
            i += 1
        return head
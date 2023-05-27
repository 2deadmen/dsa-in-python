# # Definition for singly-linked list.
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
        list1=[]
        list2=[]
        while l1!=None:
            list1.append(l1.val)
            l1=l1.next
        while l2!=None:
            list2.append(l2.val)
            l2=l2.next
        res1 = int("".join(map(str, list1)))
        res2= int("".join(map(str, list2)))
        sum=res1+res2
        result=[]
        for d in str(sum):
            result.append (int(d))
        result.reverse()
        result.append(None)
        resnode=ListNode()
        head=resnode
        for i in result:
            resnode.val=i
            newNode=ListNode()
            resnode.next=newNode
        return head
  
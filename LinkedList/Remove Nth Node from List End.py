'''
Remove Nth Node from List End
Asked in:  
HCL
Amazon
Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, h, N):
        if h.next == None:
            h = None
            return h
        elif h == None:
            return h
        else:

            count = 0
            current_node = h
            while current_node is not None:
                # increase counter by one
                count = count + 1
                # jump to the linked node
                current_node = current_node.next
            if N > count:
                return h.next
            th=h
            th2=th
            N=count-N
            if N==0:
                h=h.next
                return h
            N-=1
            while N!=0:
                th=th.next
                N=N-1
            if th.next.next==None:
                th.next=None
                return th2
            th.next=th.next.next
            return th2
        
                 




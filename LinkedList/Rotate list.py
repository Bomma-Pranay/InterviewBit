'''
Rotate List
Asked in:  
Amazon
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    def rotateRight(self, h, k):
        if h==None or h.next==None:
            return h
        dum=h
        ln=0
        while dum:
            ln+=1
            dum=dum.next
            
        k=k%ln
        td=h
        k=ln-k
        x=1
        while x<k:
            td=td.next
            x+=1
        dummy=h
        while dummy.next!=None:
            dummy=dummy.next
        
        dummy.next=h
        newh=td.next
        td.next=None
        return newh
        


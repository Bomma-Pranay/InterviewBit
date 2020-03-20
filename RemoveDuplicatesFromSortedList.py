'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, h):
        if h==None or h.next==None:
            return h
        th=h
        curr=h.next
        prev=h
        while curr!=None:
            while curr!=None and prev.val==curr.val:
                curr=curr.next
            prev.next=curr
            prev=curr
            if curr!=None :
                curr=curr.next
        return th

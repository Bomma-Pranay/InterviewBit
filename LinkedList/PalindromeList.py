'''
# Definition for singly-linked list.
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, h):
        if h==None or h.next==None :
            return 1
        th=h
        l=[]
        while th:
            l.append(th.val)
            th=th.next
        th=h
        cnt=-1
        while th:
            if th.val!=l[cnt]:
                return 0
            cnt-=1
            th=th.next
        return 1
        
        


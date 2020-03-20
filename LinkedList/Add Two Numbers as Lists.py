'''
Add Two Numbers as Lists
Asked in:  
Amazon
Qualcomm
Microsoft
Facebook
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, t1, t2):
        d=ListNode('a')
        td=d
        c=0
        s=0
        while t1!=None and t2!=None:
            s=t1.val+t2.val+c
            c=s//10
            s=s%10
            d.next=ListNode(s)
            d=d.next
            t1=t1.next
            t2 = t2.next
        while t1!=None:
            d.next = ListNode((c+t1.val)%10)
            d = d.next
            c=(c+t1.val)//10
            t1=t1.next
            
        while t2!=None:
            d.next = ListNode((c+t2.val)%10)
            d = d.next
            c=(c+t2.val)//10
            t2=t2.next
        if c>0:
            d.next = ListNode(c)
            d = d.next
        return td.next


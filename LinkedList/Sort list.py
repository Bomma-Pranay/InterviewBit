'''
Sort List
Asked in:  
Google
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def middle(h,flag):
    s,f=h,h
    while f!=None and f.next!=None and f.next.next!=None:
        s=s.next
        f=f.next.next
    if flag==True:
        #print(s.data)
        return s
    #print(s.next.data)
    return s.next
def merge(h1, h2):
    d = ListNode('a')
    td=d
    while h1 != None and h2 != None:
        if h1.val < h2.val:
            d.next = h1
            h1 = h1.next
        else:
            d.next = h2
            h2 = h2.next
        d = d.next
    if h1 != None:
        d.next = h1
    if h2 != None:
        d.next = h2
    return td.next
def mergeSort(h):
    if h==None or h.next==None:
        return h
    m=middle(h,True)
    sh=m.next
    m.next=None
    return merge(mergeSort(h),mergeSort(sh))

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, h):
        return mergeSort(h)

'''
Merge Two Sorted Lists
Asked in:  
Microsoft
Yahoo
Amazon
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
'''

class Node:
    def __init__(self, data):
       
        self.data = data

        # store reference (next item)
        self.next = None
        return

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, h1, h2):
        d=Node('a')
        td=d
        while h1 != None and h2 != None:
            if h1.data < h2.data:
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

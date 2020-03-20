'''
Reverse Link List II
Asked in:  
Facebook
Microsoft
Amazon
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, h, m, n):
            if h==None or h.next==None:
                return h
            cnt=h
            c=1
            while c<m:
                c+=1
                cnt=cnt.next
            newhead=ListNode('a')
            td=newhead
            while c<n:
                x=ListNode(cnt.val)
                newhead.next=x
                c+=1
                cnt=cnt.next
                newhead=newhead.next
            x=ListNode(cnt.val)
            newhead.next=x
            c+=1
            if cnt!=None:
                cnt=cnt.next
            newhead=newhead.next
            
            newhead=td.next
            #newhead=reverse(newhead)
            p=ListNode(None)
            while newhead!=None:
                t=newhead.next
                newhead.next=p
                p=newhead
                newhead=t
            #return p
            newhead=p
            re=newhead
            while re.next.val!=None:
                re=re.next
            re.next=None
            
            cnt=h
            c=1
            prev=h
            if m==1:
                h=newhead
            else:
                while c<m:
                    c+=1
                    prev=cnt
                    cnt=cnt.next
                x=cnt
                prev.next=newhead
            while c<n:
                c+=1
                cnt=cnt.next
            
            tail=newhead
            while tail.next!=None:
                tail=tail.next
            if tail and cnt:
                tail.next=cnt.next
            return h

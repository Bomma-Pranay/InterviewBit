'''
Reorder List
Asked in:  
Amazon
Microsoft
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
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
def delete_by_pos( head,pos):

    #Sir's code
    th=head
    th2=th
    if pos<0 or pos>=length(head):
        print('invalid index')
        return th
    if pos==0:
        print('pos is 0')
        head=head.next
        return head
    pos-=1
    while pos!=0:
        th=th.next
        pos=pos-1
    th.next=th.next.next
    return th2

def length(head):

    count = 0
    current_node = head

    while current_node is not None:
        # increase counter by one
        count = count + 1

        # jump to the linked node
        current_node = current_node.next

    return count

def reverse(head):
    if head==None or head.next==None:
        return head
    p=ListNode(None)
   
    #t=None
    while head!=None:
        t=head.next
        head.next=p
        p=head
        head=t
    #return p
    head=p
    head=delete_by_pos(head,length(head)-1)


    return head
def joining(h,sh):
    if h==None:
        return sh
    if sh==None:
        return h
    d=ListNode('a')
    d.next=h
    y=sh.next
    prev=sh
    while h!=None and sh!=None:
        x=h.next
        h.next=sh
        prev=y
        y=sh.next
        sh.next=x
        h=sh.next
        sh=y
    if sh!=None:
        prev.next=sh
    return d.next

def solve(h):
    m=middle(h,True)
    sh=m.next
    m.next=None
    return joining(h,reverse(sh))

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, h):
        return solve(h)
        


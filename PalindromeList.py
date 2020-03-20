 Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.
 Solution:
 
 def isPalindrome(self, h):
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

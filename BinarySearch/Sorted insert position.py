'''
Sorted Insert Position
Asked in:  
Yahoo
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, l, x):
        lo=0
        hi=len(l)-1
        ans=-1
        f=0
        while lo<=hi:
            mid=(lo+hi)//2
            if l[mid]==x:
                ans=mid
                f=1
                break
            elif l[mid]<x:
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        if f==1:
            return (ans)
    
        return (ans+1)

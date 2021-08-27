""" Similar Auestion Asked in Flipkart. Really Mind Boggling"""
"""
You are given N number of books. Every ith book has Ai number of pages. 
You have to allocate books to M number of students. There can be many ways or permutations to do so. 
In each permutation, one of the M students will be allocated the maximum number of pages. 
Out of all these permutations, the task is to find that particular permutation in which the maximum number 
of pages allocated to a student is minimum of those in all the other permutations and print this minimum 
value. Each book will be allocated to exactly one student. Each student has to be allocated at least 
one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order 
(see the explanation for better understanding).

Example 1:

Input:
N = 4
A[] = {12,34,67,90}
M = 2
Output:
113
Explanation: 
Allocation can be done in following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90}  Maximum Pages =113
Therefore, the minimum of these cases is 
113, which is selected as the output.

Example 2:

Input:
N = 3
A[] = {15,17,20}
M = 2
Output:
32
Explanation:
Allocation is done as 
{15,17} and {20}

Your Task:
You don't need to read input or print anything. Your task is to complete the function findPages() 
which takes 2 Integers N, and m and an array A[] of length N as input and returns the expected answer.

"""

"""
Solution:

We have to apply Binary Search here. Doesn't matter the array is sorted or not. 
As the books are taken in contagious manner.
"""

class Solution:
    def isValid(self,A,N,M,mid):
        student=1
        count=0
        for i in range(N):
            count+=A[i]
            if(count>mid):
                count=A[i]
                student+=1
            if student>M:
                return False
        return True
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        start =max(A)
        end=sum(A)
        res=-1
        while(start<=end):
            mid=(start+end)//2
            if(self.isValid(A,N,M,mid)):
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends
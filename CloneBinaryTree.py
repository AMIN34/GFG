#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Solution:
    def copy(self,root,d):
        if not root:
            return None
        clone = Node(root.data)
        d[root]=clone
        clone.left = self.copy(root.left,d)
        clone.right = self.copy(root.right,d)
        return clone

    def attach(self,res,root,d):
        if not root:
            return None
        root.random=d[res.random]
        self.attach(res.right,root.right,d)
        self.attach(res.left,root.left,d)

    def cloneTree(self,tree):
        if not tree:
            return None
        mymap={}
        mymap[None]=None
        res=self.copy(tree,mymap)
        self.attach(res,tree,mymap)


class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInord(a,b):
    if (not a and not b):
        return 1
        
    if(a and b) :
        t=(int)((a.data==b.data) and printInord(a.left,b.left) and printInord(a.right,b.right))
        
        if(a.random and b.random) :
            return int(t and a.random.data==b.random.data)
            
        if (a.random==b.random) :
            return t
            
        return 0
    #if a.random.data==b.random.data and printInord(a.left,b.left) and printInord(a.right,b.right):
        #return 1
    return 0


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        map=dict()

        n=int(input())
        arrnode=[x for x in input().split()]

        root=None
        i=0
        while i<3*n:

            n1,n2,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

            if n1 in map:
                parent=map[n1]
            else:
                parent = Node(n1)
                map[n1] = parent

                if not root:
                    root = parent


            child=Node(n2)
            map[n2]=child

            if lr=='R':
                parent.right=child

            elif lr=='L':
                parent.left=child

            else:
                parent.random=map[n2]


            i+=3

        ansTree=Solution().cloneTree(root)

        if ansTree==root:
            print(0)
        else:
            print(int(printInord(root,ansTree)))

#driver code ends
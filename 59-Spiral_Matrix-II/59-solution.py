class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        temp=[[0 for j in range(n)] for i in range(n)]
        val=1
        k = 0
        l=0
        x=n
        y=n
        while(val<=n*n):
            for j in range(l,y):
                temp[k][j]=val
                val+=1
            k+=1
            for i in range(k,x):
                temp[i][y-1]=val
                val+=1
            y-=1
            j=y-1
            while(j>=l):
                temp[x-1][j]=val
                val+=1
                j-=1
            x-=1
            i=x-1
            while(i>=k):
                temp[i][l]=val
                val+=1
                i-=1
            l+=1
        return temp
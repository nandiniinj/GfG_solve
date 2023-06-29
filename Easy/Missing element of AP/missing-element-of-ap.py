#User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        # code here
        a=arr[0]
        l=arr[-1]
        d=(l-a)//n
        
        for i in range(n-1):
            if arr[i]+d!=arr[i+1]:
                return arr[i]+d
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMissing(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
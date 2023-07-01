#User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        # code here
        #time complexity of the below code is O(n)
        a=arr[0]
        l=arr[-1]
        d=(l-a)//n
        
        for i in range(n-1):
            if arr[i]+d!=arr[i+1]:
                return arr[i]+d
        
        #we have to solve with time complexity of O(logn)
    
        # d=(arr[-1]-arr[0])//n
        # low=0
        # high=n-1
        
        # #binary search
        # while(low<high):
            
        #     mid=(low+(high-low))//2
            
        #     if low+1==high:
        #         return (arr[high]+arr[low])//2
        #         break
            
        #     elif (arr[mid]==(arr[0]+mid*d)):
        #         low=mid
            
        #     else:
        #         high=mid

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
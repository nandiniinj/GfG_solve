#User function Template for python3

class Solution:
	def binary_to_decimal(self, str):
		# Code here
		n=int(str)
		i=0
		dec=0
		while(n>0):
		    last=n%10
		    n=n//10
		    dec=dec+last*2**i
		    i=i+1
	    return dec
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution();
		ans = ob.binary_to_decimal(str)
		print(ans)
# } Driver Code Ends
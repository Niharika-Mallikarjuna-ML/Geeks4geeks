#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    if(n<=1):
	        return 0
	    if(arr[0]==0):
	        return -1
	   
	    jumps=0
	    max_n = 0
	    current_end=0
	    for i in range(n-1):
	        max_n = max(max_n,i+arr[i])
	        if(current_end == i):
	            current_end = max_n
	            jumps+=1
	            if(current_end >= n-1):
	               return jumps
	    return -1
	            
	        
	        
	    

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
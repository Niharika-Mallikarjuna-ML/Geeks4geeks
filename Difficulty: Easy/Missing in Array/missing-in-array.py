#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        list1 = sorted(arr)
        count=1
        for i in range(n-1):
            if(count!=list1[i]):
                return count
            else:
                count+=1
        return n
    
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends
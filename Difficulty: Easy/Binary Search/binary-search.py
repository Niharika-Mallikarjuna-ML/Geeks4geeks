#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        low=0
        high = len(arr)-1
        mid = int((low+high)/2)
        while low<=high:
            mid = int((low+high)/2)
            if (k==arr[mid]):
                return mid
            elif(k<arr[mid]):
                high=mid-1
            else:
                low = mid+1
        return -1



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)

# } Driver Code Ends
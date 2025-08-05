class Solution:
    def maxLen(self, arr):
        # Your code goes here
        n = len(arr)
        mpp = {}
        maxi = 0
        summ = 0

        for i in range(n):
            summ += arr[i]
            if summ == 0:
                maxi += 1
            else:
                if summ in mpp:
                    maxi = max(max,i - mpp[summ])
                else:
                    mpp[summ] = i 

        return maxi

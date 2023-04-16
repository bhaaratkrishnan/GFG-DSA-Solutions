class Solution:
    def subArraySum(self,arr, n, s):
        currSum = arr[0]
        start = 0
        i=1
        while i <= n:
            while currSum > s and start < i - 1:
                currSum -= arr[start]
                start += 1
            if currSum == s:
                return [start + 1, i]
            if i < n:
                currSum += arr[i]
            i += 1
        return [-1]

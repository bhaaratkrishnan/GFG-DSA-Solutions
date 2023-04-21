class Solution:
    def MissingNumber(self,array,n):
        # code here
        sum_of_n = sum(range(1,n+1))
        return sum_of_n - sum(array)

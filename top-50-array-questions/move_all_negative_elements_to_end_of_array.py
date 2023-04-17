class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        lst1 = []
        lst2 = []
        for i in arr:
            if i >= 0:
                lst1.append(i)
            else:
                lst2.append(i)
        j = 0
        for i in lst1:
            arr[j] = i
            j += 1
        for i in lst2:
            arr[j] = i
            j += 1

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        lst1 = []
        lst2 = []
        #we are seperating the positive and negative elements in 2 diffrent arrays
        for i in arr:
            if i >= 0:
                lst1.append(i)
            else:
                lst2.append(i)
        j = 0
        #then we placing in order in the given array
        #starting from positive element array
        for i in lst1:
            arr[j] = i
            j += 1
        #then negative element array
        for i in lst2:
            arr[j] = i
            j += 1

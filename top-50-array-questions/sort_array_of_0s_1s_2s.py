class Solution:
    def sort012(self,arr,n):
        # counting method
        count = Counter(arr)
        j = 0 
        for i in range(count[0]):
            arr[j] = 0
            j += 1
        for i in range(count[1]):
            arr[j] = 1
            j += 1
        for i in range(count[2]):
            arr[j] = 2
            j+=1
        # pointer method 
        low = mid = 0
        high = n - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low+= 1
                mid+= 1
            elif arr[mid] == 1:
                mid+= 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

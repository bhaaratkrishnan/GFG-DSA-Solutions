class Solution:
    def duplicates(self, arr, n):
      #time : o(n)
      #space : o(1)
    	# code here
    	output_arr = []
    	for i in range(n):
    	    x = arr[i] % n
    	    arr[x] += n
    	for i in range(n):
    	    if arr[i] >= n*2:
    	        output_arr.append(i)
    	if output_arr == []:
    	    output_arr = [-1]
    	return output_arr


'''
The goal of this challenge is to take an array of 100 values and turn it into a 2D array in the format
[
[1,2,3,4,5,7,8,9,10]
[11,12,13,14,15 ...
.
.
.
..............., 100]
]
'''

# an array that looks something like [1,2,3,4,5, ... , 100]
arr = [i for i in range(1, 101)]

end = []

# Your Code Here:
num_lists = 10
def split(arr, num_lists):
	length = len(arr)
	return [ arr[i*length // num_lists: (i+1)*length // num_lists]
		for i in range(num_lists) ] 
block = split(arr,10) 
for i in block:
	print(i)

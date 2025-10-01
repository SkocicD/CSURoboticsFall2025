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
import random

# an array that looks something like [1,2,3,4,5, ... , 100]
arr = [i for i in range(1, 101)]
random.shuffle(arr)

end = []

# Your Code Here:
placeholder = 0
index = 0
loop = True
while loop == True:
	smallin = index
	for i in range(index,100):
		if arr[i] < arr[smallin]:
			smallin = i
	placeholder = arr[index]
	arr[index] = arr[smallin]
	arr[smallin] = placeholder
	index += 1
	if index == 100:
		loop = False
print(arr)

outarr = []
index = 0
for i in range(0,10):
	inarr = []
	for x in range(0,10):
		inarr.append(arr[index])
		index += 1
	outarr.append(inarr)
for inarr in outarr:
	print(inarr)

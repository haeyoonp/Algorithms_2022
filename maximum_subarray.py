import math

def max_crossing_subarray(A,low,mid,high):
	l_sum = -10000000
	t_sum = 0
	max_left = max_right = mid
	for i in range(mid, low-1, -1):
		t_sum += A[i]
		if t_sum > l_sum:
			l_sum = t_sum
			max_left = i
	r_sum = -100000000
	t_sum = 0
	for j in range(mid+1, high+1):
		t_sum += A[j]
		if t_sum > r_sum:
			r_sum = t_sum
			max_right = j
	return (max_left,max_right,l_sum+r_sum)


def max_subarray(A,low,high):
	if high == low:
		return (low, high, A[low])
	else:
		mid = math.floor((low+high)/2)
		(l_low,l_high,l_sum) = max_subarray(A,low,mid)
		(r_low,r_high,r_sum) = max_subarray(A,mid+1,high)
		(c_low,c_high,c_sum) = max_crossing_subarray(A,low,mid,high)
		if l_sum >= r_sum and l_sum >= c_sum:
			return (l_low,l_high,l_sum)
		elif r_sum >= l_sum and r_sum>= c_sum:
			return (r_low,r_high,r_sum)
		else:
			return (c_low,c_high,c_sum)
				

fp = open("input.txt", "r")
A = list(map(int, fp.readlines()[0].split(" ")))
max_subarray(A, 0, len(A)-1)

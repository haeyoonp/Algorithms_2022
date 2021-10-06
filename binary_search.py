import math

def binary_search(A,p,r,v):
	if p<=r:
		q = math.floor((p+r)/2)
		if A[q] == v:
			return q
		if A[q] < v:
			return binary_search(A,q+1,r,v)
		else:
			return binary_search(A,p,q-1,v)


A = [1,2,3,4,5]
v = binary_search(A,0,len(A)-1,3)
print(v)
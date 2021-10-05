import math

def count_inversion(A,p,q,r):
	n1 = q - p + 1
	n2 = r - q
	L = [0]*(n1+1)
	R = [0]*(n2+1)
	for i in range (0,n1):
		L[i] = A[p + i]
	for j in range (0,n2):
		R[j] = A[q + 1+ j]
	L[n1] = 100000
	R[n2] = 100000
	i = j = 0
	for k in range (p,r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	i = j = inversions = 0
	for k in range (p,r+1):
		if 2*R[j] < L[i]:
			inversions = inversions + n1 - i
			j += 1
		else:
			i += 1
	return inversions

def big_inversion(A,p,r):
	inversions = left = right = 0
	if p<r:
		q = math.floor((p+r)/2)
		right = big_inversion(A,p,q)
		left = big_inversion(A,q+1,r)
		inversions += count_inversion(A,p,q,r)
		if left!= None:
			inversions += left
		if right!=None:
			inversions += right
		return inversions

A = [2,9,8,6,1,2,5]
v = big_inversion(A,0,len(A)-1)
print(v)
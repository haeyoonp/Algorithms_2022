import math
## v1
def merge_inversion(A,p,q,r):
	inversion = 0;
	B = [0]*(r+1)
	p_idx = p
	q_idx = q+1
	for i in range(p, r+1):
		if q_idx == r+1 or (A[p_idx] <= A[q_idx] and p_idx != q+1):
			B[i] = A[p_idx]
			p_idx += 1
		else:
			B[i] = A[q_idx]
			q_idx += 1
			inversion += 1
	for i in range(p,r+1):
		A[i] = B[i]
	return inversion


## v2
def merge_inversion2(A,p,q,r):
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
	i = 0
	j = 0
	inversions = 0
	for k in range (p,r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			inversions = inversions + n1 - i
			A[k] = R[j]
			j = j + 1
	return inversions

def inversion(A,p,r):
	inversions = left = right = 0
	if p<r:
		q = math.floor((p+r)/2)
		right = inversion(A,p,q)
		left = inversion(A,q+1,r)
		inversions += merge_inversion2(A,p,q,r)
		if left!= None:
			inversions += left
		if right!=None:
			inversions += right
		return inversions

A = [2,3,1,2]
v = inversion(A,0,len(A)-1)
print(v)
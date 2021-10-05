import math

def merge_inversion(A,p,q,r):
	inversion = 0;
	B = [0]*(r+1)
	p_idx = p
	q_idx = q+1
	for i in range(p, r+1):
		if q_idx == r+1 or (A[p_idx] <= A[q_idx] and p_idx != q+1):
			B[i] = A[p_idx]
			p_idx += 1
		elif p_idx == q+1 or (A[q_idx] <= A[p_idx] and q_idx != r+1):
			B[i] = A[q_idx]
			q_idx += 1
			inversion += 1
	for i in range(p,r+1):
		A[i] = B[i]
	return inversion

def inversion(A,p,r):
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



A = [2,3,8,6,1]
v = big_inversion(A,0,len(A)-1)
print(v)
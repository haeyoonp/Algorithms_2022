import math

def Merge(A, p, q, r):
	B = [0]*(r+1)
	p_idx = p
	q_idx = q+1
	for i in range(p, r+1):
		print(p_idx, q_idx)
		if q_idx == r+1 or (A[p_idx] <= A[q_idx] and p_idx != q+1):
			B[i] = A[p_idx]
			p_idx += 1
		elif p_idx == q+1 or (A[q_idx] <= A[p_idx] and q_idx != r+1):
			B[i] = A[q_idx]
			q_idx += 1
	for i in range(p,r+1):
		A[i] = B[i]
def merge_sort(A, p, r):
	if p<r:
		q = math.floor((p+r)/2)
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		Merge(A, p, q, r)


def insertion_sort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while -1<i and key<A[i]:
			A[i+1] = A[i]
			i += -1
		A[i+1] = key

fp = open("input.txt", "r")
A = list(map(int, fp.readlines()[0].split(" ")))
merge_sort(A, 0, 8)
#insertion_sort(A)
print(A)

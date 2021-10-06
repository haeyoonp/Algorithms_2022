import math

def Merge(B,A,q):
	A1 = A.pop(q)
	A2 = A.pop(q)
	a1 = len(A1)
	a2 = len(A2)
	C = [0]*(a1+a2)
	p_idx = 0
	q_idx = 0
	for i in range(0, a1+a2):
		if q_idx == a2 or (p_idx != a1 and A1[p_idx] <= A2[q_idx]):
			C[i] = A1[p_idx]
			p_idx += 1
		else:
			C[i] = A2[q_idx]
			q_idx += 1
	A.append(C)
def merge(B,A,k):
	while 1<k:
		q = math.floor(k/2)-1
		Merge(B,A,q)
		k = len(A)
	return A[0]
	# time complexity : nlogk

def merge_subarray(A):
	S = [0,len(a0),len(a0)+len(a1),len(a0)+len(a1)+len(a2),len(a0)+len(a1)+len(a2)+len(a3)]
	B = [0]*(len(a0)+len(a1)+len(a2)+len(a3)+1)
	A2 = []
	for ele in A:
		A2 += ele
	A2.sort()
	#merge(B,A,S,0,S[len(A)-1])
	# time complexity : nlogn 


a0 = [1,3,6,9,10]
a1 = [5,6,7,8,9]
a2 = [2,3,4,6,7]
a3 = [1,2,4,5,6]
A = [a0,a1,a2,a3]
B = [0]*(len(a0)+len(a1)+len(a2)+len(a3)+1)
#merge_subarray(A)
print(merge(B,A,len(A)))


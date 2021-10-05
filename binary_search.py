import math

def binary_search(A,p,r,v):
	if A[p] == v:
		return p
	if A[r] == v:
		return r
	q = math.floor((p+r)/2)
	if A[q] < v:
		return binary_search(A,q+1,r,v)
	else:
		return binary_search(A,p,q,v)



A = [1,2,30,41,52,63,70,81]
v = binary_search(A,0,len(A)-1,70)
print(v)
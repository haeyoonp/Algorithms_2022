import math

def binary_search(A,p,r,v):
	if p<r:
		if A[p] == v:
			return True
		if A[r] == v:
			return True
		q = math.floor((p+r)/2)
		if A[q] < v:
			return binary_search(A,q+1,r,v)
		else:
			return binary_search(A,p,q,v)

def find_twonumber(A,s):
	A.sort()
	for i in range (0,len(A)):
		found = binary_search(A[i:],0,len(A)-1-i,s-A[i])
		if found == True:
			return found
	return False

def find_twonumber2(A,s):
	A.sort()
	for i in range(0,len(A)):
		j = len(A)-1
		while i<j:
			if A[i] + A[j] == s:
				return True
			else:
				j -= 1		

A = [2,3,1,2,5,6,9,2]
print(find_twonumber2(A,20))

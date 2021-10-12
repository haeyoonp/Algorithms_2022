def parent(i):
	return i//2

def left(i):
	return i*2

def right(i):
	return 2*i+1

def max_heapify(A,i,hs):
	l = left(i)
	r = right(i)
	#print("m heapify start ",i,l,r,A[1:])
	if l<= hs and A[l] > A[i]:
		largest = l
	else:
		largest = i
	if r<= hs and A[r] > A[largest]:
		largest = r
	if largest != i:
		A[i],A[largest] = A[largest],A[i]
		max_heapify(A,largest,hs)
	#print("m heapify end",A[1:])

def build_max_heap(A):
	hs = len(A)
	for i in range((len(A[1:])-1)//2,0,-1):
		max_heapify(A,i,hs)

def heapsort(A,hs):
	build_max_heap(A)
	#print(A[1:])
	for i in range(len(A)-1,0,-1):
		A[1],A[i] = A[i],A[1]
		hs -= 1
		max_heapify(A,1,hs)
	#print(A[1:])

A = [-10000,10,3,4,2,1,3,6,2]
heapsort(A,len(A[1:]))
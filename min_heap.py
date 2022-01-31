from math import inf

# Implementing Min Heap

left   = lambda i : 2*i + 1 
right  = lambda i : 2*(i + 1)
parent = lambda i : (i - 1) // 2 

# Given a heap, adjust the heap from index i to the end
def min_heapify(H, i):
    n = len(H)
    pos = i

    l, r = left(i), right(i)
    # exchange root with the smallest child
    if l < n and H[l] < H[i]   : pos = l
    if r < n and H[r] < H[pos] : pos = r
    
    if pos != i:
        H[pos], H[i] = H[i], H[pos]
        # repeat algorithm on the new position
        min_heapify(H, pos)

# Given a list, convert it to a heap
def build_min_heap(H):
    n = len(H)
    # heapify for each non-leaf vertices
    for i in range((n // 2) - 1, -1, -1):
        min_heapify(H, i)

# Print the minimum key and delete its node
def extract_min(H):
    try: Min = H[0]
    except IndexError: print("Empty Heap!")

    # put the last element at the root and heapify at the root
    H[0] = H.pop()
    min_heapify(H, 0)
    return Min

# Decrease the value of node i in the heap
def heap_decrease_key(H, i, val):
    if H[i] < val: return "Value is not smaller!"
    
    H[i] = val
    # heapify upwards
    while i > 0 and H[parent(i)] > H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)

# Insert a leaf with key inf and decrease its 'key' to val
def heap_insert(H, val):
    H.append(inf)
    heap_decrease_key(H, len(H) - 1, val)
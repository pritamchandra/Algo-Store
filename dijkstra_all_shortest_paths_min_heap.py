# All shortests paths from single source with Dijkstra
# implemented using min heap

from math import inf

# The keyed min heap is a pair of arrays (H, H_index). The linear
# array H stores the min heap with respect to values of nodes. 
# Each node is a {key, value} dictionary.
 
# The array H_index is such that H_index[i] stores the address of
# key i in the min heap H.

left   = lambda i : 2*i + 1 
right  = lambda i : 2*(i + 1)
parent = lambda i : (i - 1) // 2 

# Swap two nodes of a heap by swapping the respective values in H
# and indices in H_index
def heap_swap(H, H_index, i, j):
    H[i], H[j] = H[j], H[i]
    H_index[H[i]['key']], H_index[H[j]['key']] = \
        H_index[H[j]['key']], H_index[H[i]['key']]

# Given a heap, adjust the heap from index i to the end
def min_heapify(H, H_index, i):
    n = len(H)
    pos = i

    l, r = left(i), right(i)
    # exchange root with the smallest child
    if l < n and H[l]['val'] < H[i]['val']   : pos = l
    if r < n and H[r]['val'] < H[pos]['val'] : pos = r
    
    if pos != i:
        heap_swap(H, H_index, i, pos)
        # repeat algorithm on the new position
        min_heapify(H, H_index, pos)

# Given a list, convert it to a heap
def build_min_heap(H):
    n = len(H)
    # Create H_index 
    H_index = [i for i in range(n)]

    # heapify for each non-leaf vertices
    for i in range((n // 2) - 1, -1, -1):
        min_heapify(H, H_index, i)

    return H_index

# Print the minimum key and delete its node
def extract_min(H, H_index):
    if not H: return("Empty Heap!")

    Min = H[0]
    # put the last element at the root
    try:
        H[0] = H.pop()
        H_index[H[0]['key']] = 0

    # exception: the heap contains a single element
    except IndexError: pass

    H_index[Min['key']] = None
    # heapify the root
    min_heapify(H, H_index, 0)
    return Min

# Decrease the value of node i in the heap
def heap_decrease_key(H, H_index, key, Val):
    i = H_index[key]
    if H[i]['val'] < Val: return "Value is not smaller!"
    
    H[i]['val'] = Val
    # heapify upwards
    while i > 0 and H[parent(i)]['val'] > H[i]['val']:
        p = parent(i)
        heap_swap(H, H_index, i, p)
        i = p

# Dijkstra main
def dijkstra(G, s = 0):
    n = len(G)                    # Number of vertices
    dist = [inf]*n; dist[s] = 0   # Distance vector of the graph
    parents = [[None]]*n          # Parent vector of the graph

    # build a min-priority-queue with node-distance as key-value pairs
    Q = [{'key' : u, 'val' : dist[u]} for u in range(n)]
    Q_index = build_min_heap(Q)

    while Q:
        u = extract_min(Q, Q_index)['key']
        for v in range(n):
            # visit the neighbours v of u
            if v != u and G[u][v] != inf:
                new_dist = dist[u] + G[u][v]
                
                # relax the edge u -> v
                if new_dist < dist[v]:
                    dist[v] = new_dist; parents[v] = [u]
                    heap_decrease_key(Q, Q_index, v, new_dist)

                # v may have multiple parents in its shortest path  
                # The following condition is the sole modification from single
                # shortest path to all shortest paths in Dijkstra's algorithm 
                elif new_dist == dist[v]:
                    parents[v] += [u]

    return dist, parents

# construct all shortest paths
def construct_paths(u, parents):
    paths = []

    def construct_path(u, P):
        for v in parents[u]:
            # keep visiting the parents until root is reached
            if v == None:
                P.reverse(); paths.append(P)
                return
            # path through node v
            construct_path(v, P + [v])

    construct_path(u, [u])
    return(paths)

# Functions are complete. Inputs below.
G = [[  0,   1,   2,   1, inf, inf],
     [  1,   0, inf, inf, inf,   1],
     [  2, inf,   0, inf,   2,   2],
     [  1, inf, inf,   0,   1,   1],
     [inf, inf,   2,   1,   0, inf],
     [inf,   1,   2,   1, inf,   0]
    ]

s = 0

dist, parents = dijkstra(G, s)

# print all shortest paths
for u in range(len(G)):
    print(construct_paths(u, parents))
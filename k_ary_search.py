# k-ary search for x inside A
from math import ceil

def k_search(A, x, k = 2):
        
    # search from index "u" to index "end"
    def search(x, u, end):
        if end == u + 1:
            # the search space is a singleton
            return (True, u) if A[u] == x else False

        # determine bucket size
        step = ceil((end - u)/k)
        v = u + step

        while v < end:
            if x <= A[v - 1]:
                # potential bucket for x is found
                return search(x, u, v)

            u, v = v, v + step

        return search(x, u, end)
    
    # begin search on the whole range
    return search(x, 0, len(A))    
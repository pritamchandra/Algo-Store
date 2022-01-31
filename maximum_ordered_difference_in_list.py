# Maximum ordered difference in a list

# input : List A
# output : max{A[v] - A[u] : u < v}
# That is, given a list A find the maximum of differences A[v] - A[u] where v > u. 

# Note, this can be used to solve the maximum sum contiguous subarray problem by 
# calling max_diff on the cumulative sum array.

def max_diff(A):
    n = len(A)

    # Cum_Min[u] = min{A[ : u]}
    Cum_Min = [A[0]]
    for i in range(1, n):
        Cum_Min.append(min(Cum_Min[-1], A[i]))

    # Cum_Max[v] = max{A[v : ]}
    Cum_Max = [A[-1]]
    for i in range(n - 2, -1, -1):
        Cum_Max.insert(0, max(Cum_Max[0], A[i]))

    # It can be shown that the solution appears in the set 
    # {Cum_Max[i + 1] - Cum_Min[i]} for some i
    sol = max([Cum_Max[i + 1] - Cum_Min[i] for i in range(n - 1)])
    return sol
# ordered k-subsets of of a set A
def ordered_subsets(A, k = 1):
    n = len(A)
    if n == k: return [A]
    if k == 1: return [[a] for a in A]

    _A = A[1:]
    subsets_with_first = ordered_subsets(_A, k - 1)
    for subset in subsets_with_first: subset.insert(0, A[0])
     
    subsets_wo_first = ordered_subsets(_A, k)
    
    return subsets_with_first + subsets_wo_first
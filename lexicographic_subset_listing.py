# lexicographic listing of subsets of an n-set
def list_subsets_lex(n):
    def next_set(current, last_index):
        print(current)

        for j in range(last_index, n):
            next_set(current + [j], j + 1)
    
    next_set([], 0)
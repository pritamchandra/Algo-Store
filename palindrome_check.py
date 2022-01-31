# check whether a given string is a palindrome
def is_palindrome(string):
    n = len(string)
    u, v = 0, n - 1
    
    while v > u:
        if string[u] != string[v]:
            return False
        u, v = u + 1, v - 1
        
    return True
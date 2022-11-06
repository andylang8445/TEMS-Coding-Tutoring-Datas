def recursion__Ans(s, l, r):
    if (l >= r):
        return 1
    elif (s[l] != s[r]):
        return 0
    else:
        return recursion__Ans(s, l+1, r-1)

def isPalindrome(s):
    return recursion__Ans(s, 0, len(s)-1)

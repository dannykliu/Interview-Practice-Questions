def lcs(s1, s2):
    '''
    Returns the length of the longest common subsequence of s1 and s2.
    '''

    # base case: the length of the LCS of an empty string and another string is 0
    if not s1 or not s2: 
        return 0

    # if the first characters of each string agree,  
    # count the character towards the LCS
    if s1[0] == s2[0]:             
        useIt = 1 + lcs(s1[1:], s2[1:]) 
    else:
        useIt = 0

    # make the problem smaller by peeling away the first character of s2 or 
    # the first character of s1 and computing the resulting LCS; choose the 
    # longer answer
    loseIt2 = lcs(s1[1:], s2)                        
    loseIt1 = lcs(s1, s2[1:])

    return max(useIt, loseIt1, loseIt2)

print(lcs('car', 'cat'))


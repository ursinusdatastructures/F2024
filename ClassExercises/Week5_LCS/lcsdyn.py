def LCS(s1, s2):
    """
    Parameters
    ----------
    s1: string
        First string
    s2: string
        Second string
    
    Returns
    -------
    string: A maximal subsequence between s1 and s2
    """
    M = len(s1)
    N = len(s2)
    table = [[0]*N for i in range(M)]
    choices = [[0]*N for i in range(M)]
    for i in range(M):
        for j in range(N):
            res = 0
            if s1[i] == s2[j]:
                res = 1
                if i > 0 and j > 0:
                    choices[i][j] = 0
                    res += table[i-1][j-1]
            else:
                res1 = 0
                res2 = 0
                if i > 0:
                    res1 = table[i-1][j]
                if j > 0:
                    res2 = table[i][j-1]
                if res1 > res2:
                    choices[i][j] = 1
                    res = res1
                else:
                    choices[i][j] = 2
                    res = res2
            table[i][j] = res
    for j in range(N):
        choices[0][j] = 2
    for i in range(M):
        choices[i][0] = 1
    i = M-1
    j = N-1
    seq = ""
    while not (i == 0 and j == 0):
        ## TODO: Fill this in. If s1[i] == s2[j], add s1[i] (or s2[j])
        ## to before what's currently in seq.
        ## Then, regardless, change i and j based on choices[i, j]
        if s1[i] == s2[j]:
            seq = s1[i] + seq
        if choices[i][j] == 0:
            i, j = i - 1, j - 1
        elif choices[i][j] == 1:
            i = i-1
        else:
            j = j-1
    if s1[0] == s2[0]:
        seq = s1[0] + seq
    return seq

s1 = "We rinsed all grease off"
s2 = "Ursinus college students are great students"

print(LCS(s1, s2))

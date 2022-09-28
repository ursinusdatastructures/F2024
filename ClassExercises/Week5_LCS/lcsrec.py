def LCS(s1, s2):
    """
    Parameters
    ----------
    s1: string
        First string
    s2: string
        Second string
    """
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + LCS(s1[0:-1], s2[0:-1])
    else:
        return max(LCS(s1[0:-1], s2), LCS(s1, s2[0:-1]))



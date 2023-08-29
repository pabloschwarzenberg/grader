M = []
def mcm(n1,n2,bla):
    M.append(n1*n2)
    if n1 > n2:
        n = n1 - n2
        while n >= n2:
            n -= n2
        if n == 0:
            return M[0]/n2
        if n != 0:
            return mcm(n2,n,0)
    if n2 > n1:
        n = n2 - n1
        while n >= n1:
            n -= n1
        if n == 0:
            return M[0]/n1
        if n != 0:
            return mcm(n1,n,0)


if __name__=="__main__":
    pass
           
def mcm(a,b,d):
    c = a*b

    A = max(a,b)
    B = min(a,b)

    while B:
        mcd = B
        B = A % B
        A = mcd
    return c/mcd

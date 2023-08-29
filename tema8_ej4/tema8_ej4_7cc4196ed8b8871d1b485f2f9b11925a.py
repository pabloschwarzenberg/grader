def rot13(n):
    x = "abcdefghijklmnopqrstuvwxyz"
    y = x[13:]+x[:13]
    z = lambda c: y[x.find(c)] if x.find(c)>-1 else c
    return ''.join( z(c) for c in n )
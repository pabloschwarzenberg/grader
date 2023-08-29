def rot13(x):
    L= []
    X= []
    K= []
    for i in x:
        L.append(i)
    for j in L:
        f= j.lower()
        X.append(f)
    for k in X:
        k= ord(k)+13
        if k > 122:
            k= chr(k- 26)
            K.append(k)
        else:
            k= chr(k)
            K.append(k)
    O= ''.join(K)
    return O
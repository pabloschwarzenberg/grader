def buscarTodas(a, b):
    A = list(a)
    b = str(b)
    p = ""
    for M in range(len(a)):

        p = p +str(A.index(b))+" "
        A[A.index(b)] = 0

        if b not in A:
            break

    p=p.rstrip()
    return p

if __name__ == "__main__":
    pass
           
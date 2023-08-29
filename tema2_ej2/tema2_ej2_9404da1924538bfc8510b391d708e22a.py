# completa el código de la función
def amigos(N, S):
    s1 = 1
    s2 = 1
    for i in range(2, N):
        if (N % i == 0):
            s1 = s1 + i
    for o in range(2,S) :
        if (S % o == 0):
            s2 = s2 + o
    if s1 == S and s2 == N:
        return True
    else:
        return False
           
# completa el código de la función
def amigos(N, S):
    global e
    e = 0
    global d
    d = 0
    for i in range(1, N):
        if (N % i == 0):
          d = d + i
    for j in range(1, S):
        if (S % j == 0):
          e = e + j
    if (d == S) and (e == N):
       return True
    else:
       return False
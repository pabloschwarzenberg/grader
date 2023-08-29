def amigos(A,B):
    sumaA = 0
    sumaB = 0
    for i in range(1,A):
        if A%i == 0:
            sumaA += i

    for n in range(1,B):
        if B%n == 0:
            sumaB += n

    return sumaA == B and sumaB == A
    if sumaA == B and sumaB == A:
         return True
    else :
         return False 
  


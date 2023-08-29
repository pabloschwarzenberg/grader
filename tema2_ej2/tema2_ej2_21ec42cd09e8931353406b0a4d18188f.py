# completa el código de la función
def amigos(R,E):
    U=0
    S=0
    for i in range(1,R):
        if R%i==0:
            U+=i
    for i in range(1,E):
        if E%i==0:
            S+=i
    if S==R and U==E:
        return True 
    else:
        return False
   
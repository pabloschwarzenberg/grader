# completa el código de la función
def suma(N,S):
       for i in range(2,N):
             if(N % i==0):
                    S=S+i
       return S

def amigos(N,S):
    sum1,sum2=1,1
    sum1 = suma(N, sum1)
    sum2 = suma(S, sum2)
    if((sum1==S)and (sum2==N)):
        return True
    else:
        return False


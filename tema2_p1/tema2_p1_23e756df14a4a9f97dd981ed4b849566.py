# por favor escribe aquí tu función
N=7
def es_primo (N):
    contador=0
    for i in range(1,N+1):
        if N%i==0:
          contador=contador+1
    if contador ==2:
       return  True
    else:
       return False
print(es_primo(N))     
           
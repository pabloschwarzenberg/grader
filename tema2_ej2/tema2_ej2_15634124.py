# completa el código de la función
def amigo(a,b):
    divisores = []
    i=1
    while i<a:
        if a%i==0:
            divisores.extend([i])
            print(divisores)
        i=i+1
    suma=0 
    for j in range(0,len(divisores)):
        suma=suma+divisores[j]
    if b==suma:
       return True
    if b!= suma:
       return False
    
def amigos(a,b):
    if amigo(a,b) and amigo(b,a):
        return 1    
    else:    
        return 0
    
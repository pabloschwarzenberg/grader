# completa el código de la función
def suma_divisores(a):
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
    if suma == 1:
        return (suma, True)
    else:
        return (suma, False)
  
           
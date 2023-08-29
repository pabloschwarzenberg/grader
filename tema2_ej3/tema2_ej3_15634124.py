def numero_perfecto(a):
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
    if suma == a:
        return True 
    else: 
        return False
        

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
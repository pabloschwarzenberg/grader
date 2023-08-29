def numero_perfecto(a):
    lista =[]
    suma=0
    for i in range (1,a):
        lista.append(i)
    for k in lista:
        if a % k==0:
            suma+=k
        print(suma)
    
    if suma == a:
        return True
    else:    
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
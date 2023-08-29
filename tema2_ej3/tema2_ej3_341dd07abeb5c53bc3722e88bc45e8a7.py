def numero_perfecto(a):
    cont=1
    suma=0
    while cont!=a:
        if a%cont==0:
            suma=suma+cont
        cont=cont+1
    if suma==a:
        return True
    if suma!=a:
        return False

   
   
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
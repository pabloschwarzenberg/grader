def numero_perfecto(a):
    suma=1
    inicio=2
    for i in range(inicio,a-1):
         if a%inicio==0:
            suma=suma+inicio
            inicio=inicio+1
         else:
             inicio=inicio+1
    if a==1 or a!=suma:
        return False
    else:
        return True


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
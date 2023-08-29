def numero_perfecto(a):
    suma=0
    for i in range(1,a):
     if a%i==0:
         print(i)
         suma+=i
    print(suma)     
    respuesta=""
    if suma==a: 
     respuesta=True
    else: 
     respuesta=False
    return respuesta



if __name__=="__main__":
    a=int(input("introduzca el número a dividir: "))
    print("El resultado es:",numero_perfecto(a))

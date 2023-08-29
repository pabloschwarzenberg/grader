numero=int(input("diga el numero"))
   
def suma_divisores(numero):
    lista=[]
    i=0
    while(i<numero-1):
        i+=1
        if(numero%i==0):
            lista.append(i)


    suma=0
    for i in lista:
     suma += i

    if(suma==1):
        print("Es primo")
    else:
        print("No es primo")


suma_divisores(numero) 

    
   
    

  
           
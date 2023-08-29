
def numero_perfecto(n) :
    suma = 0
    for i in range(1,n):
        if(n%i==0):
            suma = suma+i
    return suma
    
n = int(input("ingrese numero: "))
 
        
if (n == numero_perfecto(n)):
        print("El numero",n,"es perfecto")
else:
        print("El numero",n,"no es perfecto")

    
for numero in range(1,n):
    suma = 0
    for n2 in range(1,numero - 1):
        if (numero % n2 == 0):
            suma = suma + n2
    if(suma == numero):
        print("otros numeros perfectos",numero)     
           
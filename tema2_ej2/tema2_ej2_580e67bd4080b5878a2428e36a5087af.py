# Definición de la función de comprobación de números amigos
def numeros_amigos(x,y):
    suma_x=0
    suma_y=0
    for i in range(1,x):
        if x%i==0:
            suma_x+=i

    for k in range(1,y):
        if y%k==0:
            suma_y+=k

    if(suma_x == y):
        return True
    elif(suma_y == x):
        return True
    else:
        return False
 
    
n1 = int(input("Ingrese el primer numero\n"))
n2 = int(input("Ingrese el segundo numero\n"))

print(numeros_amigos(n1,n2))           
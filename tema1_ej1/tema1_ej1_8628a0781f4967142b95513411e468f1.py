#Suma de los N primeros números
n= int(input("Ingrese la cantidad de primeros numeros que desea sumar: "))
while True: 
    if n > 0:
     suma_n = (n* (n+1)) /2
     print("El resultado de la suma es: ", suma_n)
     break 
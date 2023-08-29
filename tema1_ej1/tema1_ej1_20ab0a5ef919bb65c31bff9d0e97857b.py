#Suma de los N primeros números
x=0
while True:
    try:
        x=int(input("Ingrese un numero para sumar sus primeros numeros naturales : "))
        if(x>=0):
            break
    except ValueError:
        continue

print( (x*(x+1)/2) )   
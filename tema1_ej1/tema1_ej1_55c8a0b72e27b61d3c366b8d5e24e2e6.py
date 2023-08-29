#ingrese un numero natural
#la suma de los primeros 3 numeros naturales
N=int(input("numero natural: "))
while not(N>=0):
    N = int(input("n no puede ser - a 0"))
    
#calculo de la suma de los numeros naturales
resultadodelasuma=N*(N+1)/2
print("el resultado de la suma es: ", resultadodelasuma) 

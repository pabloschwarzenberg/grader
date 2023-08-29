#Juego adivina mi número
n=14
j=0
i=5
while((j !=n) and (i>0)):
    j= int(input("Ingrese un número: "))
    if(j > n):
        print("El numero es menor.")
    elif(j < n):
        print("El numero es mayor.")
    i-=1
if(j==n):
    print("Adivinaste, el numero era: ", n)
else:
    if(i==0):
        print("No adivinaste, el número era: ",n)
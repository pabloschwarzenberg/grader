#Juego adivina mi número

n=int(input("Ingrese un numero del 1 al 20:"))
m=8
x=1

while n!=m and x<=5:
    if x<5:
        if n<m:
            print("Mi numero es mayor")
        elif n>m:
            print("Mi numero es menor")
        n=int(input())
        x=x+1
    
    else:
        print("No adivinaste, mi numero era",m)
        break
if n==m:
    print("Adivinaste, mi número era:",m)
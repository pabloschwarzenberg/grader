#Factores Primos
n= int(input("Ingrese un numero entero:"))
if n== 2:
    print (n)
for i in range (2,n):
    if (n%i) == 0:
        if i == 2:
            print (i)
        elif i == 1 or i ==0:
            break

        elif i > 2:
            for j in range (2, i):
                if i % j ==0:
                    break
                elif i % j != 0 and j == (i-1):
                    print (i)


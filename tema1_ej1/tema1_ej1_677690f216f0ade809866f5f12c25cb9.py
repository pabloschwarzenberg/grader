#Suma de los N primeros números
n=int(input("ingrese un numero cualquiera: "))
## Estos son los números naturales: 1, 2, 3, 4, 5, 6, 7, infinito....
##
## n=3
## 1+2+3: suma=6
## 3(3+1)/2 = 12/2 = 6 <- llegamos al mismo 6!!
##
## n=5
## 1+2+3+4+5: suma=15
## 5(5+1)/2 = 30/2 = 15 <- llegamos al mismo 15!!
##
suma=n*(n+1)
div=suma/2
print(div)
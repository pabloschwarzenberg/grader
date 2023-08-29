#Ordenar tres números
a= int(input("ingrese el primer numero"))
b= int(input("ingrese el segundo numero"))
c= int(input("ingrese el tercer numero"))

N= max(a, b, c)
m= min (a, b ,c)
i= (a+b+c)- N - m
print("el orden de los numeros seria:" ,m,",",i,",",N)
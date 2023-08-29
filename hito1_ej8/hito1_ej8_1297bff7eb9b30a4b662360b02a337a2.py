#Descomponer un número
n=int(input("Ingrese un numero de hasta 4 digitos: "))

miles=n//1000
cen=(n-(miles*1000))//100
dec=(n-(miles*1000)-(cen*100))//10
uni=(n-(miles*1000)-(cen*100)-(dec*10))//1

print(miles,"M +",cen,"C +",dec,"D +",uni,"U")
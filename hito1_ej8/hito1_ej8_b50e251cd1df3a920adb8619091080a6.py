#Descomponer un número
#Descomponer un número

num=int(input("escribe un numero de 4 digitos: "))

um=num//1000

c=(num-(um*1000))//100

d=(num-(um*1000+c*100))//10

u=(num-(um*1000+c*100+d*10))//1

print(um,"M+",c,"C+",d,"D+",u,"U")
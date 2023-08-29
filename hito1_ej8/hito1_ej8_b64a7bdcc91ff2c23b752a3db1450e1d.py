#Descomponer un número
numero= eval(input("ingrese un numero de 4 digitos ",))
m= (numero//1000)
c= (numero%1000)
c2= c//100
d=(numero%100)
d2= d//10
u= (numero%10)
print(m,"M +",c2,"C +",d2,"D +",u,"U")
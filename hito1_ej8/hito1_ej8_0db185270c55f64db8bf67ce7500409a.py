#Descomponer un número
a=int(input("Ingresa un número de 4 cifras: "))
#residuo de la division
b=int((a-(a%1000))/1000)
c=int((a%1000/100))
d=int((a%100)/10)
e=a%10
print("Descomposición: ",b,"M +",c,"C +",d,"D +",e,"U") 
#Descomponer un número
num = int(input("Ingrese un numero: "))
u = int(num%10)
d = int((num%100)/10)
c = int((num%1000)/100)
m = int((num%10000)/1000)
 
print( m,"M +",c,"C +",d,"D +",u,"U")
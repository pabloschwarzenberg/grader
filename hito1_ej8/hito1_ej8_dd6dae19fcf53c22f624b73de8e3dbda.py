#Descomponer un número
numero= int(input("Ingresa un número: "))

while len(str(numero))>4:
    numero= int(input("Ingresa un número: "))

for i in range(0,3):
    miles= (numero - (numero % 1000))/1000
    modulo=numero%1000

    centena= (modulo - (modulo % 100))/100
    modulo2=modulo%100

    decena= (modulo2 - (modulo2 % 10))/10

    unidad=modulo2%10

    
if len(str(numero))==4:
    print(str(int(miles)) + "M + " + str(int(centena))+ "C + " + str(int(decena)) + "D + " + str(unidad) +"U")

if len(str(numero))==3:
    print(str(int(centena))+ "C + " + str(int(decena)) + "D + " + str(unidad) +"U")

if len(str(numero))==2:
    print(str(int(decena)) + "D + " + str(unidad) +"U")

if len(str(numero))==1:
    print(str(unidad) +"U")
      
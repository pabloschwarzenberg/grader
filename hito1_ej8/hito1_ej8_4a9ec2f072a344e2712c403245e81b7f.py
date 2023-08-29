#Descomponer un número
print ("Descomponiendo los números")
numero = int(input("Ingrese un número de 4 cifras: "))
while numero > 9999:
    numero = int(input("Error. Ingrese un número de 4 cifras: "))

cuarto = numero//1 % 10
tercero = numero//10% 10
segundo = numero//100 % 10
primero = numero//1000 % 10
if primero >0 :
    primero = str(primero)+"M +"
else:
    if primero <=0:
        primero = ""
if segundo >0:
    segundo = str(segundo)+ "C +"
else:
    if segundo <=0:
        segundo = ""
if tercero >0:
    tercero = str(tercero)+"D +"
else:
    if tercero <=0:
        tercero =""
if cuarto >0:
    cuarto = str(cuarto)+"U"
else:
    if cuarto <=0:
        cuarto = ""
print(format(primero),format(segundo),format(tercero),format(cuarto))
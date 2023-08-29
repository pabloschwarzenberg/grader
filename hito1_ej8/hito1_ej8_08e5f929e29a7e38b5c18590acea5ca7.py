#Descomponer un número
numero = eval(input("ingrese maximo 4 digitos: "))
mil = int(numero//1000)
cien = int(numero%1000)//100
diez = int(numero%100)//10
unidad = int(numero%10)//1
if mil==0:
    print(cien,"C+", diez,"D+", unidad,"U")
if mil==0 and cien==0:
    print(diez,"D+", unidad,"U")
if mil==0 and cien==0 and diez==0:
    print(unidad,"U")
if mil>=0:
    print(mil,"M+",cien,"C+", diez,"D+", unidad,"U")
#Descomponer un número
numero = int(input("ingrese un numero hasta cuatro digitos: "))
while (numero<0 and numero>9999):
    numero = int(input("erroor ingrese un numero hasta cuatro digitos: "))
cadena = str(numero)
largo = len(cadena)
if(largo==4):
    m = cadena[0]
    c = cadena[1]
    d = cadena[2]
    u = cadena[3]
    print(m,"M +",c,"C +",d,"D +",u,"U")
if(largo==3):
    c = cadena[0]
    d = cadena[1]
    u = cadena[2]
    print(c,"C +",d,"D +",u,"U")
if(largo==2):
    d = cadena[0]
    u = cadena[1]
    print(d,"D +",u,"U")
if(largo==1):
    u = cadena[0]
    print(u,"U")

      
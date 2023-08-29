numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese segundo numero: "))
contador=1
suma=0
while contador <= numero:

    if numero % contador==0:
        suma+= contador
        #print(suma)

    elif suma==numero2:
        a=1
        break
    contador +=1

contador2=1
suma2=0
while contador2 <= numero2:

    if numero2 % contador2==0:
        suma2+= contador2
      #  print(suma2)

    elif suma2==numero:
        b=1
        break
    contador2 +=1

if a==b:
    print("True")
else:
    print("False")
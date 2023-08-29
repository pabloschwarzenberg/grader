#Contestador de celular
num=int(input("Ingrese numero telefonico:"))
hr=int(input("Ingrese hora de la llamada:"))
digitos=num%1000

if hr>0 and hr<7:
    print("Resultado: CONTESTAR")

elif hr>=19:
    print("Resultado: NO CONTESTAR")

elif hr>=7 and hr<=14:
    if digitos==909:
       print("Resultado: CONTESTAR")
    else:
       print("Resultado: NO CONTESTAR")

elif hr<19 and hr>17:
    if digitos==877:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
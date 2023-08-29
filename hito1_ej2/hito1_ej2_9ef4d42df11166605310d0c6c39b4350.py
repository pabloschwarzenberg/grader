#Contestador de celular
celular = int(input("ingrese numero telefonico de 8 digitos: "))
hora = int(input("ingrese la hora: "))

c6 = celular % 10 
c7 = int((celular % 100) /10)
c8 = int((celular % 1000) /100)
c1 = int((celular % 100000000) /10000000)
c2 = int((celular % 10000000) /1000000)
c3 = int((celular % 1000000) /100000)
if hora >= 0 and hora <= 7:
    print("contestar")
    
if hora <= 14 and hora > 7 and c6==9 and c7==0 and c8==9:
    print("contestar")

if hora >= 17 and hora <= 19 and c1==8 and c2==7 and c3==7:
    print("no contestar")
else:
    if hora >= 17 and hora <= 19:
        print("contestar")
if hora > 19:
    print("no contestar")

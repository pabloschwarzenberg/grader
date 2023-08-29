#Contestador de celular
num = int(input("ingrese numero telefonico>> "))
hora = int(input("ingrese hora de llamada>> "))

Num = str(num)
listaNum = Num.split()

if len(listaNum) == 8:
    if 0 <= hora <= 7:
        print("contestar")
    if hora < 14 and num[5:7] == 909:
        print("contestar")
    if 17 <= hora <= 19 and num[0:2] == 877:
        print("contestar")
    if 19 < hora:
        print("no contestar")
else:
  print("no contestar")
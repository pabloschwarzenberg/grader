#Contestador de celular
num=int(input("Ingrese número telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))
contestar=False
if hora in range(0,7):
    print("Contestar")
if hora in range(8,14):
    num=str(num)
    if num[-3:]=="909":
        print("Contestar")
if hora in range(17,19):
    num=str(num)
    print(num[:3])
    if num[:3]=="877":
        print("No contestar")
    else:
        print("Contestar")
if hora in range(19,24):
   print("No contestar")    
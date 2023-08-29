#Contestador de celular
numero=str(int(input("Digite numero de telefono: ")))
if len(numero)!= 8:
    print("Numero de telefono invalido")
hora=int(input("Ingrese hora de llamada: "))
while True:
    if hora > 0 and hora < 7:
        print("NO CONTESTAR")
        break
    if hora < 14:
        print("CONTESTAR")
        break
    if numero.find("909",5,7):
        print("NO CONTESTAR")
        break
    if hora > 17 and hora < 19:
        print("NO CONTESTAR")
        break
    if numero.find("877",0,2):
        print("CONTESTAR")
        break
    if hora > 19 and hora < 23:
        print("CONTESTAR")
        break     
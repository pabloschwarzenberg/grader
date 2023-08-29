#Contestador de celular
numero=str(int(input("Numero telefonico")))
if len(numero)!= 8:
    print("Numero invalido")
    

hora=int(input("Hora de la llamada"))

while True:
    if hora > 0 and hora < 7:
        print("No contestar")
        break
    
    if hora < 14:
        print("Contestar")
        break
    if numero.find("909",5,7):
        print("No contestar")
        break

    if hora > 17 and hora < 19:
        print("No contestar")
        break
    if numero.find("877",0,2):
        print("Contestar")
        break

    if hora > 19 and hora < 23:
        print("Contesto")
        break
    
T = int(input("Ingrese un numero telefonico :"))
H=int(input("Ingrese hora de la llamada :"))

llamada = str(T)
ultimo_numero = llamada[5:8]
primer_numero = llamada[0:3]

if  (H>=0) and (H<=7):
    print("Contestado 1")
elif (H<=14) and (ultimo_numero !="909"):
    print("No contestado")
elif(H<=14) and (ultimo_numero =="909"):
    print("Contestar")
elif(H>= 15) and (H <= 19) and (primer_numero != "877"):
    print("Contestar")
else:
    print("No contestar final")
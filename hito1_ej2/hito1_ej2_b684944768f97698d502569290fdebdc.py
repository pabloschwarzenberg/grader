#Contestador de celular
num =int(input("Ingrese el numero telefonico: "))
hora = int(input("Ingrese la hora de la llamada(0 al 23): "))
num =str(num)

if (hora>=0 and hora<=7) or (hora<14 and (num[5]=="9") and (num[6]=="0") and (num[7]=="9")) or \
   (hora>=17 and hora<=19 and num[0]!="8" and num[1]!="7" and num[2]!="7"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
    
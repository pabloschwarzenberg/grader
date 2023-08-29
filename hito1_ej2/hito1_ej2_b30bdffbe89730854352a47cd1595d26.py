#Contestador de celular
num=int(input("ingrese número telefónico(8 cifras): "))
hora=int(input("ingrese hora de la llamada en formato HH de 24h: "))
resultado=""
if(hora>0 and hora<=7):
    resultado="contestar"
elif(hora>7 and hora<=14 and num%1000==909):
    resultado="contestar"
else:
    resultado="NO CONTESTAR"

print("resultado: ",resultado)
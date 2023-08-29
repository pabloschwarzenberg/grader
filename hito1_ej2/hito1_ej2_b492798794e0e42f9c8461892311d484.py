#Contestador de celular
numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese la hora de llamada:"))

ptres = numero//100000
utres = numero%1000

if(hora>=00) and (hora<=7):
    print("Contestar, llamada de emergencia")

elif(hora>=8) and (hora<=14) or (utres==909):
    print("Contestar")
else:
    print("No contestar")

if(hora>=15) and (hora<=16):
    print("No contestar")   
elif(hora>=17) and (hora<=19) or (ptres==877):
    print("Contestar")

    
if(hora>19) and (hora<=23):
    print("No contestar")


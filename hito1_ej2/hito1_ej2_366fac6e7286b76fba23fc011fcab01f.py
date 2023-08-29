#Contestador de celular
numero = int(input("ingrese numero de 8 cifras"))
hora = int(input("ingrese la hora [0-23]:"))

primerostres = numero//100000
ultimostres = numero%1000

if(hora>=00) and (hora<=7):
    print("Contestar, llamada de emergencia")

elif(hora>=8) and (hora<=14) or (ultimostres==909):
    print("Contestar")
else:
    print("No contestar")

if(hora>=15) and (hora<=16):
    print("No contestar")   
elif(hora>=17) and (hora<=19) or (primerostres==877):
    print("Contestar")

    
if(hora>19) and (hora<=23):
    print("No contestar")
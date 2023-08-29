#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
while not (len(str(numero)) == 8 ):
    numero = int(input("Ingrese numero telefonico: "))

      
hora = int(input("Ingrese hora de la llamada: "))   
while not (hora>=0 and hora<=23):
  hora = int(input("Ingrese hora de la llamada: "))

last=numero%1000
if (hora>=0 and hora<=7):
    resultado ="CONTESTAR"
elif(hora<14):    
    if (last==909):
        resultado ="CONTESTAR" 
    else:
        resultado = "NO CONTESTAR"
elif (hora>=17 and hora <=19):
     if(last==877):
         resultado="CONTESTAR"
     else:
         resultado="NO CONTESTAR"
else:
    resultado="NO CONTESTAR"         
print("Resultado: ",resultado)        
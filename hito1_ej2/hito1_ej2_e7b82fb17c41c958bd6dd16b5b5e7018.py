#Contestador de celular
numero=int(input("ingrese un numero de telefono de 8 cifras: "))
hora=int(input("ingrese hora: "))
resto=numero%1000

if(hora>=0 and hora<=7):
    print("contestar")
if(hora>7 and hora<14 and resto==909):
    print("contestar")
          
if(hora>14 and hora<17 and resto==877):
    print("contestar")
if(hora>=17 and hora<=19 and resto!=877):
    print(" no contestar")
if(hora>19):
    print("no contestar")
          
    

          
             
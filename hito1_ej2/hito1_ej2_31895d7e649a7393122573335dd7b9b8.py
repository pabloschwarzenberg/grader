#Contestador de celular
n_celular= (input("ingrese numero telefonico de 8 digitos"))
hora= int(input("ingrese hora de llamada"))
if(hora >= 0 and hora <= 7):
     print("CONTESTAR")
#s=str (n_celular)

#print(str(n_celular[-3])

elif (hora < 14 and (int(str(n_celular[-3])) == 9) and (int(str(n_celular[-2]))== 0) and (int(str(n_celular[-1])) == 9)):
      print("CONTESTAR")
      
elif(hora >= 17 and hora<= 19) and (int(str(n_celular[-8])) == 8) and (int(str(n_celular[-7]))== 7) and (int(str(n_celular[-7])) == 7):
     print("NO CONTESTAR")
else:
     if(hora >= 17 and hora<= 19):
      print("CONTESTAR")

if(hora > 19):
     print("NO CONTESTAR")
      

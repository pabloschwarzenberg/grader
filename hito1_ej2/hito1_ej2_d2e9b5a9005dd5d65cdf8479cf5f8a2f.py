#Entrada
hora = input("hora de la llamada: ")
n_telefonico = input("Numero telefonico de 8 digitos: ")

#Desarrollo 
x = (0,1,2,3,4,5,6,7,8,9)
n_telefonico= x and x and x and x and x and x and x and x

if (hora < str(8)):
   print("Contestar")
elif hora > str(7) and hora < str(14):
   print("No contestar")
elif hora > str(16) and hora < str(19):
   print("Contestar")
elif hora > str(19):
   print("No contestar")
      
   
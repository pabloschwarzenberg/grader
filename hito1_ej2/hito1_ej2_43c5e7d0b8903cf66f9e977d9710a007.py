#Contestador de celular

print("Ingrese numero de 8 digitos: ")
num=int(input())
print("ingrese hora llamada: ")
hora=eval(input())
NumFinales=num%1000
print("Parte final del numero es: ", NumFinales)
NumIniciales=num//100000
print("Parte inicial del numero es: ", NumIniciales)

if (0<=hora<=7):
 print("Contestar")
else:
    if (7<=hora<=14):
     if (NumFinales==909):
      print("Contestar")
     else:
      print("No contestar")
    else:
        if (17<=hora<=19):
         if (NumIniciales==877):
          print("No contestar")
         else:
          print("Contestar")
        else:
            if (19<=hora):
             print("No Contestar")
        

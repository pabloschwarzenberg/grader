#Contestador de celular
n_telefono = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de llamada: "))

if(n_telefono >= 99999999):
    print("Número inválido")
   
if(hora >=0 and hora <=7):
    print("CONTESTAR")
elif(hora <14 and n_telefono % 1000 ==909):
    print("CONTESTAR")
elif(hora <14):
    print("NO CONTESTAR")
elif(hora >=17 and hora <=19 and n_telefono // 1000 >=877):
    print("NO CONTESTAR")
elif(hora >=17 and hora <=19):
    print("CONTESTAR")
elif(hora > 19):
    print("NO CONTESTAR")      
#Contestador de celular
 
numero = int(input("ingrese su numero de tlfn: "))

hora = int(input("ingrese hora de llamada: "))

#n1 son los primeros(3) numeros y n2 son los ultimos(3) numeros
numero1 = (numero//100000)
numero2 = (numero%1000)

if hora >= 0 and hora <= 7:
    print("contestar")
    
elif numero2 == 909 and hora >= 8 and hora <= 14:
    print("contestar")
    
elif numero2 != 909  and hora >= 8 and hora <= 14:
    print("no contestar")
    
elif  hora >= 17 and hora == 19:
    print("contestar")
    
elif numero1 == 887 and hora >= 17 and hora == 19:
    print("no contestar")
    
else:
    hora > 19
    print("no contestar")
#Contestador de celular
numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de llamada: "))

if 7 >= hora >= 0 : 
    print("contestar")
elif 7 <= hora < 14 :
    if  numero%1000==909:
        print("contestar")
    else:    
        print("no contestar")
elif 17 >= hora >=19:
    if numero//100000==877:
        print("contestar")
    else:
        print("no contestar")
else:
    print("no contestar")
   

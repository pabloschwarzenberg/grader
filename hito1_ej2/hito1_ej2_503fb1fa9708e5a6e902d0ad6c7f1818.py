#Contestador de celular
numero=(input("ingrese el numero de telefono:"))

largo= len(numero)

if largo == 8:
    hora= (input("ingrese la hora en la cual esta llamando:"))
    
    num4= (numero[0])
    num5= (numero[1])
    num6= (numero[2])
    num1= (numero[5])
    num2= (numero[6])
    num3= (numero[7])
    
    if hora == "0" and "7" :
        print("contestar")
    elif hora > "7" and hora < "14":
        print("No contestar")
    elif num1== "9" and num2 == "0" and num3== "9":
        print("contestar")
    elif hora == "17" and "19":
        print("contestar")
    elif num4== "8" and num5== "7" and num6== "7":
        print("no contestar")
    elif hora > "19":
        print("no contestar")
else:
    print("el numero tiene que ser de 8 digitos")     
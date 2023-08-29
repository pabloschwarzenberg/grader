#Contestador de celular

Telefono = int(input("Ingrese un número telefónico: "))
Hora = int(input("Ingrese una hora: "))
Cadena = str(Telefono) 
Lista = list(Cadena)
Digitos = len(Lista)

while (Hora > 23 or Hora < 0):
    print("La hora no puede ser inferior a 0 o mayor a 23")
    Hora = int(input("Ingrese una hora: "))
while(Digitos != 8):
    print("El número ingresado debe ser mayor a 8 digitos")
    Telefono = int(input("Ingrese un número telefónico: "))

Digito1 = Lista[5]
Digito2 = Lista[6]
Digito3 = Lista[7]

if (Hora <= 7):
    print("Resultado: Contestar")
elif (7 < Hora and Hora <= 14):
    if (Digito1 + Digito2 + Digito3 == "909"):
        print("Resultado: Contestar")
    
    elif (Digito1 + Digito2 + Digito3 != "909"):
        print("Resultado: No Contestar")

elif(17 <= Hora <= 19):
    if (Digito1 + Digito2 + Digito3 == "877"):
        print("Resultado: Contestar")

    elif (Digito1 + Digito2 + Digito3 != "877"):
        print("Resultado: No Contestar")

elif (Hora > 19):
    print("Resultado: No Contestar")
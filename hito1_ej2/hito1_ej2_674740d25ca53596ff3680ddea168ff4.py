#Contestador de celular:
#Solicitud de datos:
telefono = int(input("Ingrese numero telefonico (este debe contener 8 cifras): ")) 
hora = int(input("Ingrese hora de la llamada (como número entero entre 0 y 23): "))
#Casos hipotéticos:
if (hora >= 0) and (hora <= 7):
    print("teléfono:", telefono)
    print("hora:", hora)
    print("resultado: contestar")
elif (hora > 7) and (hora < 14):
    if telefono % 1000 == 909: # Verificar si el número termina en 909
        print("teléfono:", telefono)
        print("hora:", hora)
        print("resultado: contestar")
    else:
        print("teléfono:", telefono)
        print("hora:", hora)
        print("resultado: NO contestar")
elif (hora >= 17) and (hora <= 19):
    if telefono // 1000000 == 877: # Verificar si el número comienza por 877
        print("teléfono:", telefono)
        print("hora:", hora)
        print("resultado: contestar")
    else:
        print("teléfono:", telefono)
        print("hora:", hora)
        print("resultado: NO contestar")
elif (hora > 19) and (hora <= 23):
    print("teléfono:", telefono)
    print("hora:", hora)
    print("resultado: NO contestar")
else:
    print("teléfono:", telefono)
    print("hora:", hora)
    print("resultado: NO contestar")
      
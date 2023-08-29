#contestadora automatica

telefono = '12345678'
x = input("ingrese su número: ")
telefono = x
hora = int(input("ingrese una hora: "))
if len(telefono) == 8:
    if hora >= 0 and hora <= 23:
        if hora <= 7: 
            print(telefono)
            print(hora)

            print("CONTESTAR")  
        elif hora <= 14:
            print(telefono)
            print(hora)
            print("NO CONTESTAR")
        elif hora <= 14 and telefono[5:] == 909:
            print(telefono)
            print(hora)
            print("CONTESTAR")
        elif hora < 19 and hora > 17 and telefono[:4] == 877:   
            print(telefono)
            print(hora)
            print("CONTESTAR")
        elif hora > 19:
            print(telefono)
            print(hora)
            print("NO CONTESTAR")
    else:
        print("esa hora no existe.")
else: 
    print("los numeros de telefono solo tienen 8 digitos.")

      
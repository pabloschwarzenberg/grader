numero_telefono = int(input("ingrese numero telefonico: "))
hora_llamada = int(input("ingrese hora de la llamada: "))

if 10000000 <= numero_telefono <= 99999999 and 0 <= hora_llamada <= 23:
    if 0 <= hora_llamada <= 7:
        print("Contestar")
    if 8 <= hora_llamada <= 14:     
        ultimos_tres_digitos = numero_telefono % 1000
        if ultimos_tres_digitos == 909:
            print("Contestar")
        else:
            print("No contestar")
            
        
    if 15 <= hora_llamada <= 16:
        print("No contestar")
        
    if 17 <= hora_llamada <= 19:
        primeros_tres_digitos = numero_telefono // 100000
        if primeros_tres_digitos == 877:
            print("No contestar")
        else:
            print("Contestar")
        

    if 20 <= hora_llamada <= 23:
        print("No contestar")
    else:
        ("No se encuentra disponible")
      
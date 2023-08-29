#Contestador de celular
def resultado(telefono,hora):
    valor = str(telefono)
    ultimo_digito = int(valor[-3:])
    print(valor[:3])
    print(ultimo_digito)
    print(valor)

    if 0 <=hora<=7:
        return True

    elif 7<hora<=14 and (909==int(valor[-3:])):
        return True

    elif 17<=hora<=19 and(int(valor[:3])!=877):
        return True
    
    else:
        return False

celular = int(input("Ingrese el numero : "))
hora =int(input("Ingrese la hora"))

if resultado(celular,hora):
    print("Contestar")

else:
    print("No contestar")
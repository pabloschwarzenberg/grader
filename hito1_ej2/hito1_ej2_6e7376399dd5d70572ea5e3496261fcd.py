#Contestador de celular
numero=str(input("ingrese numero telefonico: "))
hora=int(input("ingrese la hora: "))
terminacion=int(numero[5:8])
inicio=int(numero[0:3])
if ((hora>=0) and (hora<=7)):
    print("resultado: Contestar")
elif hora<14 and terminacion==909:
        print("resultado: Contestar")
elif hora<14:
    print("Resultado: No contestar")
elif hora>=17 and hora<=19 and inicio==877:
    print("Resultado: No contestar")
elif hora>=17 and hora<=19:
    print("Resultado: Contestar")
elif hora>19:
    print("Resultado: No contestar")      
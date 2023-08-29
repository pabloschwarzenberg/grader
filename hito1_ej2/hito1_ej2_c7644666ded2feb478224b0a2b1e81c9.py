numero = int(input("Ingresa un número telefonico:"))
while(len(str(numero)) > 8 or len(str(numero)) < 8 ):
    numero = int(input("Ingresa un número telefonico:"))

hora = int(input("Ingresa la hora: "))
while(hora > 23 or hora < 0 ):
    hora = int(input("Ingresa la hora:"))
ultimo_digito = int(str(numero)[5:8])
primeros_digitos = int(str(numero)[0:2])

if(hora >= 0 and hora <= 7):
    print("Resultado: CONTESTAR")
elif(hora < 14 and ultimo_digito != 909):
    print("Resultado:NO CONTESTAR")
elif(ultimo_digito == 909):
    print("Resultado: CONTESTAR")
elif(hora >= 17 and hora <= 19) and (primeros_digitos == 877):
    print("Resultado: CONTESTAR")
elif(hora > 19):
    print("Resultado:NO CONTESTAR")
else:
    print("Resultado:NO CONTESTAR")


#Zodiaco
#ENTRADA
dia = int(input("Ingresa tu día de cumpleaños: "))
mes = input("Ingresa tu mes de nacimiento: ")
#PROCESO
if (dia >= 21 or dia <= 20) and (mes == marzo or mes == abril ):#Aries
    print("Aries")
elif (dia >= 20 or dia <= 21) and (mes == abril or mes == mayo ):
    print("Tauro")
elif (dia >= 21 or dia <= 21) and (mes == mayo or mes == junio ):
    print("Geminis")
elif (dia >= 21 or dia <= 23) and (mes == junio or mes == julio ):
    print("Cancer")
elif (dia >= 23 or dia <= 23) and (mes == julio or mes == agosto ):
    print("Leo")
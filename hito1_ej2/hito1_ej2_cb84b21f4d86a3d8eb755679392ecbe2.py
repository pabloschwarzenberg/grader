#Contestador de celular
sizePhone = 1
errorHour = 1

while sizePhone != 8:

    intPhone=input("Ingrese numero telefonico: ")    

    sizePhone = (len(intPhone))

    if sizePhone != 8 :
        print("El numero telefonico debe tener 8 digitos")
    

while errorHour == 1:

    intHour=input("Ingrese hora de la llamada: ")  

    sizeHour = (len(intHour))

    intHour = int(intHour)

    if sizeHour > 2 or intHour < 0 or intHour > 23:
        print("Hora incorrecta")
    else:
        errorHour = 0

startPhone = intPhone[0:3]
endPhone = intPhone[5:8]
print("startPhone:", startPhone)

intPhone = int(intPhone)
startPhone = int(startPhone)
endPhone = int(endPhone)

if intHour >= 0 and intHour < 8:
    print("CONTESTAR")
elif intHour < 15 and endPhone == 909:
     print("CONTESTAR")
elif intHour > 16 and intHour < 20 and startPhone != 877:
     print("CONTESTAR")
elif intHour > 19:
     print("NO CONTESTAR")
else :
    print("NO CONTESTAR")     
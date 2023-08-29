telefono=int(input(">>> Ingrese numero telefonico: "))
hora=int(input(">>> Ingrese hora de la llamada: "))
res=0

if hora >= 0 and hora <= 7:
    print("Contestar")

elif hora >= 8 and hora < 14:
    res = telefono % 1000
    if res==909:
        print("Contestar")
    else: print("No contestar")

elif hora >= 17 and hora <= 19:
    res2 = telefono//1000
    print(res2)
    if res2 == 877:
        print("Contestar")
    else: print("No contestar")
#Después de las 19:00, no contestas el celular.
elif hora >= 20 and hora <= 23:
    print("No contestar")
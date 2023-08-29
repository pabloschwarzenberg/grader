#Contestador de celular
num=int(input("¿Qué número la esta llamando?: "))
hora=int(input("¿Qué hora es?: "))

if hora >= 0 and hora <= 7:
    print("Responder")

elif hora > 7 and hora < 14:
    if num % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 14 and hora < 17:
    print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:
    if num // 100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora > 19 and  hora <=23:       
    print("NO CONTESTAR")     
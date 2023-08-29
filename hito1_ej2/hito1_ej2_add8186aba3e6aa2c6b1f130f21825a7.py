numero = int(input("¿Qué número llama?: "))
hora = int(input("¿A qué hora es la llamada?: "))

if hora <= 7:
    print("CONTESTAR")
elif hora <= 14:
    if numero%1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= numero <= 19:
    if numero%1000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
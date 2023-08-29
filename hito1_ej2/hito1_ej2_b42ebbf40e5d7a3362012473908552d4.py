a=int(input("Ingrese el numero telefonico:"))
b=int(input("Ingrese la hora de la llamada:"))
if a > 99999999 or a < 11111111 or b > 23 or b < 0:
    print("Valores no validos")
else:
    c = str(a)
    d=c[5]
    e=c[6]
    f=c[7]

    if b >= 0 and b <= 7:
        print("CONTESTAR")
    elif 14 > b and 7 < b and d == "9" and e == "0" and f == "9":#("9","0","9") == (d,e,f):
        print("CONTESTAR")
    elif b < 14 and b > 7 and d != "9" and e != "0" and f != "9":#("9","0","9") != (d,e,f):
        print("CONTESTAR")
    elif b >= 17 and b <= 19 and d != "8" and e != "7" and f != "7":
        print("NO CONTESTAR")
    elif b >= 17 and b <= 19 and d == "8" and e == "7" and f == "7":
        print("NO CONTESTAR")
    elif b > 19:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
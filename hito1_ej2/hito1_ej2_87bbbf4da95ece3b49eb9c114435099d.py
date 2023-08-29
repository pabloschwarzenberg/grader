a = int(input("Ingrese número telefonico:"))
while len(str(a)) > 8 or len(str(a)) < 8:
    a = int(input("Ingrese número telefonico:"))

b = int(input("Ingrese hora de la llamada:"))
while b < 0 or b > 23:
    b = int(input("Ingrese hora de la llamada:"))

sa = str(a)

if b >= 0 and b <= 7:
    print(">>>>>CONTESTAR")
elif (sa[5] == "9" and sa[6] == "0" and sa[7] == "9") and (b > 7 and b <= 14):
    print(">>>>>CONTESTAR")
elif (b > 7 and b <= 14):
    print(">>>>>NO CONTESTAR")
elif b > 14 and b < 17:
    print(">>>>>NO CONTESTAR")
elif (sa[0] == "8" and sa[1] == "7" and sa[2] == "7") and (b >= 17 and b <= 19):
    print(">>>>>NO CONTESTAR")
elif b >= 17 and b <= 19:
    print(">>>>>CONTESTAR")
elif b > 19 and b <=23:
    print(">>>>>NO CONTESTAR")
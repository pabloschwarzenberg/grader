cel = int(input("Ingrese numero: "))
h = int(input("Ingrese hora: "))
ult = cel%1000
pri = cel
while pri >= 1000:
    pri = pri//10

if h <= 7:
    print("CONTESTAR")
elif h < 14 and ult == 909:
    print("CONTESTAR")
elif h >= 17 and h <= 19 and pri != 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
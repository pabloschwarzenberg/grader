n = int(input("Ingrese el número telefonico:  "))
h = int(input("Ingrese hora de la llamada:  "))
n3 = n - ((n // 1000) * 1000)
x3 = n//100000
#78735653
if 9999999 < n < 100000000 and 0 <= h <=23:

    if 0 <= h <= 7:
        print("CONTESTAR")
    elif 7 < h < 14 or n3==909:
        print("CONTESTAR")
    if 17 <= h <= 19 and x3!=877:
        print("CONTESTAR")
    elif 17 <= h <= 19 and x3==877:
        print("NO CONTESTAR")
    if 19 <= h <= 23:
        print("NO CONTESTAR")
else:
    print("los datos son incorecctos")
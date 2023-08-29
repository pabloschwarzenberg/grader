num = int(input("Ingrese numero"))
hr = int(input("ingrese hora"))
if hr >= 0 and hr <= 7:
    print("CONTESTAR")
elif hr >= 8 and hr <= 14:
    if num%1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hr >= 17 and hr <= 19:
    if num//100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
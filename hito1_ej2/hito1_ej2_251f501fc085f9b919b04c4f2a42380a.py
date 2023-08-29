hr = int(input("Hora del día: "))
nm = int(input("Número telefónico: "))

if hr > 19 or hr <= 23:
    print("NO CONTESTAR")
elif hr >= 0 and hr <= 7:
    print("CONTESTAR")
elif hr >= 17 or hr <= 19 and nm >= 87700000 or nm <= 87799999:
    print("NO CONTESTAR")
elif hr >= 17 or hr <= 19:
    print("CONTESTAR")
elif  hr > 8 and hr < 14:
    print("NO CONTESTAR")

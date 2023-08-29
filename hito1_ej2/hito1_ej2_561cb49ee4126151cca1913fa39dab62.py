     caller = int(input("Ingrese número telefónico: "))
hour = int(input("Ingrese hora de la llamada: "))

# proceso
caller_number = str(caller)
caller_digits = len(caller_number)


if hour >= 0 and hour <= 7:
    print("CONTESTAR")

elif hour <= 14 and caller_number[5:8] == '909':
    print("CONTESTAR")
else:
    print("NO CONTESTAR")

    if hour >= 17 and hour <= 19 and caller_number[0:3] == '877':
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if hour > 19:
    print("NO CONTESTAR")
NU = int(input("NUMERO: "))
HO = int(input("HORA: "))
NUSTR = str(NU)

if HO > 0 and HO < 7:
    print("CONTESTAR")
elif HO < 14:
    if NUSTR[-3:] == "909":
        print("CONTESTAR")
    else:
        print("NO CONSTESTAR")
elif HO > 17 and HO < 19:
    if NUSTR[3:] == "877":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif HO > 19:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")
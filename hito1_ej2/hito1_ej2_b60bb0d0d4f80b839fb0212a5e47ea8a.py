S=input("Numero de telefono:")
H=input("Hora de llamada:")
S=int(S)
H=int(H)
S=str(S)
UTRES=S[-3:]
UTRES=int(UTRES)
PTRES=S[:3]
PTRES=int(PTRES)



if 7>=H>=0:
    print("CONTESTAR")


elif UTRES==909 and 14>=H:
    print("CONTESTAR")


elif 19>=H>=17 and PTRES==877:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
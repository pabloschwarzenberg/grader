num_telefono=str(int(input("87765545")))
hora_llamada=int(input("18"))
m=num_telefono[5:8]
m=int(m)
n=num_telefono[0:3]
n=int(n)
if 7>=hora_llamada>=0:
    print("CONTESTAR")
elif m==909:
    print("CONTESTAR")
elif (19>=hora_llamada>=17 and n!=877):
    print("CONTESTAR")
elif 14>=hora_llamada:
    print("NO CONTESTAR")
elif hora_llamada>=19:
    print("NO CONTESTAR")
elif n==877:
    print("NO CONTESTAR")
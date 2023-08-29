N = int(input("Ingrese un número: "))
NU = N % 10
NDP = ((N % 100) - NU)
NCP = ((N % 1000) - NDP - NU)
NMP = ((N % 10000) - NCP - NDP - NU)

ND = NDP / 10
NC = NCP / 100
NM = NMP / 1000

if NM == 0 and NC == 0 and ND == 0:
    print(NU,"U")
elif NM == 0 and NC == 0:
    print(int(ND),"D +",NU,"U")
elif NM == 0:
    print(int(NC),"C +",int(ND),"D +",NU,"U")
else:
    print(int(NM),"M +",int(NC),"C +",int(ND),"D +",NU,"U")
L1 = list(range(2,8))
RUT = input("ingrese los numeros del rut: ")

M = 2
SA = 0


for I in range(len(RUT) - 1, -1, -1):
    X = RUT[I]
    X = int(X)
    SA = X*M + SA
    M = M + 1
    if M == 8:
        M = 2
RD = SA % 11

NF = 11-RD

if NF == 11:
    print("dv=0")

elif NF == 10:
    print("dv=K")

else:
    NF = str(NF)
    print("dv=%s" % (NF))
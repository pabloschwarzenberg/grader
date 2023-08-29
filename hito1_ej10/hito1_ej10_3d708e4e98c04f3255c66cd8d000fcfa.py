from sys import exit

usr = int(input())
key = int(input())
balAcc, balAtm, count = 100000, 1000000, 1
sel = ""

while usr != 10334151 and key != 1803:
    if count == 3:
        print("tarjeta bloqueada")
        quit()
    print("clave invalida")
    count += 1
    usr = int(input())
    key = int(input())

sel = input()
while str(sel) != "N":
    # print("ASCII for sel is:", ord(sel))
    if len(sel) == 1:
        if ord(sel) > 57 or ord(sel) < 48 :
            break
    if int(sel) > balAcc or int(sel) > balAtm:
        print("monto no permitido")
        continue
    else:
        balAcc -= int(sel)
        balAtm -= int(sel)
        print("saldo cuenta=" + str(balAcc) + "\nsaldo cajero=" + str(balAtm))
    sel = input()
usr = int(input())
key = int(input())
balAcc, balAtm, count = 100000, 1000000, 1
sel = ""
repo, taken = [20, 40, 40], [0, 0, 0] # That's 20k, 10k and 5k bills, respectively

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
    if len(sel) == 1:
        if ord(sel) > 57 or ord(sel) < 48 :
            break
    if int(sel) > balAcc or int(sel) > balAtm:
        print("monto no permitido")
        continue
    else:
        print("Else")
        factor = int(sel)/5000

        while factor > 0:
            print("Iterando")
            if factor < 2:
                repo[2] -= 1
                taken[2] += 1
                factor -= 1
            elif factor < 4:
                repo[1] -= 1
                taken[1] += 1
                factor -= 2
            else:
                repo[0] -= 1
                taken[0] += 1
                factor -= 4

        balAcc -= int(sel)
        balAtm -= int(sel)
        print("saldo cuenta=" + str(balAcc) + "\nsaldo cajero=" + str(balAtm))
        print("billetes 20000=" + str(taken[0]))
        print("billetes 10000=" + str(taken[1]))
        print("billetes 5000=" + str(taken[2]))
    sel = input()
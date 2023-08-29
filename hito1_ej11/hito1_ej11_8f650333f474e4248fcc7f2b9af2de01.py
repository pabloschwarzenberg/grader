#Cajero Automático
dinero = 1000000
cuenta = 100000
mucho = 0
diez = 0
cinco = 0

a = input()
b = input()

if a == "10334151" and b == "1803":
    c = int(input())
    cuenta -= c
    dinero -= c
    while c > 0:
        if c < 20000:
            if c < 10000:
                cinco += 1
                c -= 5000
            diez += 1
            c -= 10000
        mucho += 1
        c -= 20000
print("saldo cuenta=", cuenta, "saldo cajero=", dinero)
print("saldo cuenta=", cuenta, "saldo cajero=", dinero)
print("billetes 20000=", mucho)
print("billetes 10000=", diez)
print("billetes 5000=", cinco)
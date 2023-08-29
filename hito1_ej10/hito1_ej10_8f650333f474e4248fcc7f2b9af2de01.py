#Cajero Automático
dinero = 1000000
cuenta = 100000

a = input()
b = input()

if a == "10334151" and b == "1803":
    c = int(input())
    print("saldo cajero=", dinero - c)
    print("saldo cuenta=", cuenta - c)
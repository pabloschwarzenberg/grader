#Cajero Automático
s_c = 1000000
s_u = 100000

u  = int(input("Ingresa usuario: "))
c = int(input("Ingresa clave: "))

f = 0

while True:
    if u == 10334151 and c == 1803:
        m = int(input("Cuanto monto desea retirar: "))
        if m <= s_u and m <= s_c:
            s_u -= m
            s_c -= m
            continuar = input("PARA SALIR PRESIONA ALGO DISTINTO DE N: ")
            if continuar != "N":
                break
        elif m > s_u:
            print("monto no permitido")    
            
    elif u == 10334151 and c != 1803:
        f += 1
        if f == 3:
            print("tarjeta bloqueada")
            break
        else:
            print("clave invalida")
            c = int(input("Ingresa clave: "))
    
print("saldo cuenta =",s_u)
print("saldo cajero =",s_c)

e_b = 100000 - s_u
e_bi = e_b // 1000

#contb20 = 20
#contb10 = 40
#contb5 = 40

cantb20 = e_bi // 20
sobra = e_bi % 20
cantb10 = sobra // 10
sobraa = sobra % 10
cantb5  = sobraa // 5    

print("billetes 20000=",cantb20)
print("billetes 10000=",cantb10)
print("billetes 5000=",cantb5)
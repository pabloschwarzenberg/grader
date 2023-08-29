#Contestador de celular
numero = int(input("Ingrese numero de telefono: "))
hora = int(input("Ingrese hora de la llamada: "))

c7 = numero % 10**7
tc7 = round((numero - c7)/10**7) #digito8
c6 = c7 % 10**6
tc6 = round((c7 - c6)/10**6) #digito7
c5 = c6 % 10**5
tc5 = round((c6 - c5)/10**5) #digito6
c4 = c5 % 10**4
tc4 = round((c5 - c4)/10**4) #digito5
c3 = c4 % 10**3
tc3 = round((c4 - c3)/10**3) #digito4
c2 = c3 % 10**2
tc2 = round((c3 - c2)/10**2) #digito3
c1 = c2 % 10**1
tc1 = round((c2 - c1)/10**1) #digito2
c0 = c1 % 10**0
tc0 = round((c1 - c0)/10**0) #digito1
a = (f"{tc2}")
b = (f"{tc1}")
c = (f"{tc0}")
imp2 = [a, b, c]
d2 = int("".join(imp2))
d = (f"{tc7}")
e = (f"{tc6}")
f = (f"{tc5}")
imp1 = [d, e, f]
d3 = int("".join(imp1))

if hora >= 0 and hora <= 7:
    print("CONTESTAR")

elif hora < 14:
    
    if d2 == "909":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

elif hora >= 17 and hora <= 19:
    
    if d3 == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")
    
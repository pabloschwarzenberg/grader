#Contestador de celular
n = int(input("Ingrese numero telefonico:"))
h = int(input("Ingrese hora de la llamada:"))

if 0 <= h <= 7:
    print("CONTESTAR")

if 19 <= h <= 23:
    print("NO CONTESTAR")

n1 = n//10**5
n2 = n%10**3

if 7 <= h <= 14 and n2 != 909:
    print("NO CONTESTAR")
if 7 <= h <= 14 and n2 == 909:
    print("CONTESTAR")

if 17 <= h <= 19 and n1 != 877:
    print("CONTESTAR")
if 17 <= h <= 19 and n1 == 877:
    print("NO CONTESTAR")
      
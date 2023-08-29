#Contestador de celular
N = input("Ingrese numero telefonico:")
H = int(input("Ingrese hora de la llamada:"))
n = int(N[5:8])
p = int(N[0:3])
while True:
    if H <= 7:
        print("Resultado: CONTESTAR")
        break
    if H < 14 and n != 909:
        print("Resultado: NO CONTESTAR")
        break
    if H < 14 and n == 909:
        print("Resultado: CONTESTAR")
        break
    if H <= 19 and H >= 17 and p != 877:
        print("Resultado: CONTESTAR")
        break
    if H <= 19 and H >= 17 and p == 877:
        print("Resultado: NO CONTESTAR")
        break
    if H > 19:
        print("Resultado: NO CONTESTAR")
        break
      
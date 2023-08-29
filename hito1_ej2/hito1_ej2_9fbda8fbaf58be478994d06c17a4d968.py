#Contestador de celular
N = str(input("Indique su numero telefonico: "))
H = int(input("Indique su hora de llamada: "))

N3F = N[5:8]
N3I = N[0:3]

if H >= 0 and H <= 7:
    print("CONTESTAR")

elif H > 7 and H < 14 and N3F == "909":
    print("CONTESTAR")

elif not(N3I == "877") and H >= 17 and H <= 19 :
    print("CONTESTAR")

elif H > 19:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")



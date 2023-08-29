#Contestador de celular
n = int(input("Ingrese número telefónico: "))
h = int(input("Ingrese hora de la llamada: "))
r = "Resultado: "

N = str(n)

if (0 < h < 7) or (7 < h < 14 and N[-3:] != 909) or (17 < h < 19 and N[0:3] == 877):
    print(r, "CONTESTAR")

else:
    print(r, "NO CONTESTAR")    
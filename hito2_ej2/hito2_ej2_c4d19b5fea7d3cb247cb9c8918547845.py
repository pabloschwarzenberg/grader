cod = str(input("Ingrese genoma:"))
cod = cod.upper()
k = len(cod)
for i in range(k):
    if (cod[i] == "A" or cod[i] == "G" or cod[i] == "T" or cod[i] == "C"):
        n = "SECUENCIA CORRECTA"

    else:
        n = "SECUENCIA INCORRECTA"


print(n)
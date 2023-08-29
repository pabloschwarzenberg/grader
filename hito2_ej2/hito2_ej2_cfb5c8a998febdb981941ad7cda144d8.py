#Validar Secuencias de ADN
secuencia = input()
secuencia2 = secuencia.upper()
secuencia1 = list(secuencia2)
for i in secuencia1:
    if i != "A" and i != "C" and i != "G" and i != "T":
        x = "incorrecto"
    else:
        x = "correcto"
if x == "incorrecto":
    print("secuencia incorrecta")
else:
    print("secuencia correcta")
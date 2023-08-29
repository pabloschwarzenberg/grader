secuencia=input("Ingrese secuencia:")
secuencia=secuencia.upper()
print(secuencia)
conteo_si=0

for letra in secuencia:
    if letra=="A":
        conteo_si+=1

    elif letra=="C":
        conteo_si+=1

    elif letra=="T":
        conteo_si+=1

    elif letra=="G":
        conteo_si+=1

if conteo_si==len(secuencia):
    print("Secuencia correcta")

else:
    print("Secuencia incorrecta")      
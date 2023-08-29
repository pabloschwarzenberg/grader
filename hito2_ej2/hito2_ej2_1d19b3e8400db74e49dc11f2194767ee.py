def secuencia_ADN(secuencia):
    secuencia=secuencia.upper()

    for letra in secuencia:
       if letra not in "ACTG":
           return False 
    return True

secuencia=input("Ingresa la secuencia de ADN: ")
if secuencia_ADN(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")      
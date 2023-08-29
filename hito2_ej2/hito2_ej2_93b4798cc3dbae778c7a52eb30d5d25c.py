#Validar secuencias de ADN

secuencia=input("Secuencia de ADN:")
secuencia=secuencia.upper()

def sec():
    for i in secuencia:
        if i not in "ACTG":
            return "secuencia incorrecta"
    return "secuencia correcta"

print(sec())

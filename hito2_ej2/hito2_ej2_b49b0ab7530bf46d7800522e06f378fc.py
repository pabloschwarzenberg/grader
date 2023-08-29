def validar_genoma(secuencia):
    letras={"A","C","T","G","a","c","t","g"}
    for letra in secuencia:
        if letra not in letras:
            return False
    return True

secuencia=input("Ingrese la secuencia: ")
if validar_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      
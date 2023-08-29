def verificar(genoma):
    letras = ["A","C","T","G"]
    for letras in genoma:
            return "secuencia correcta"
    return "secuencia incorrecta"
genoma = str(input())
genoma = genoma.upper()
print(verificar(genoma))
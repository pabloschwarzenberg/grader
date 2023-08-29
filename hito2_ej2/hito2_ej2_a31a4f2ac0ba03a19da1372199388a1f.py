secuencia = input()
grandes = secuencia.upper()

genoma = ["A","C","T","G"]

for letra in grandes:
    if not letra in genoma:
        print("secuencia incorrecta")
    else:
        print("secuencia correcta")
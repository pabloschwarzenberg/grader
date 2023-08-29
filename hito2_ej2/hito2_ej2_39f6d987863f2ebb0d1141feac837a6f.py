secuencia= input("escribe una secuencia: ")
genomas= ["a","c","t","g"]
secuencia= secuencia.lower()
total= 0
for letra in secuencia:
    if letra in genomas:
        total= total + 1
if total==len(secuencia):
    print("secuencia correcta")
else: print("secuencia incorrecta")      
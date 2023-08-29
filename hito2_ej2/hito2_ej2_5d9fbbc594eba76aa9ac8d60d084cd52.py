secuencia = input("Ingrese su secuencia: ").upper()
genoma = ["A","C","T","G"]
cuenta = 0
for a in secuencia:
    if a not in genoma:
        cuenta += 1
if cuenta != 0:
    print("secuencia incorrecta")
else:
    print("secuencia correcta")
    
      
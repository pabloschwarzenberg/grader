bases=["a","A","g","G","c","C","t","T"]
secuencia=str(input("Ingrese secuencia: "))
letras=list(secuencia)
if letras in bases:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
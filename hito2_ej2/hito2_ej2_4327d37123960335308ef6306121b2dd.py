secuencia=input()
secuencia=secuencia.upper()
bases="A,C,T,G"
for letra in secuencia:
    if letra in bases:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")

      palabra = input("Ingresa una palabra")
palabra = palabra.upper()
print(palabra)
I=0
while I<len(palabra):
    if palabra[I]!="A" and palabra[I]!="C" and palabra[I]!="T" and palabra[I]!="G":
        print("secuencia incorrecta")
        I=I+1

    else:
        print("secuencia correcta")
    

palabra=input("ingresa una palabra:")
palabra=palabra.lower()

estado=True
I=0
while I < len(palabra):
   
    if palabra[I]!="a" and palabra[I]!="c" and palabra[I]!="t" and palabra[I]!="g":
        estado=False
        break

    else:
        pass    

    I=I+1

if estado == False:
    print("secuencia incorrecta")
else:
    print("secuencia correcta")
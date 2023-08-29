palabra=input("ingrese palabra")
palabra=palabra.upper()
print(palabra)
i=0
cuenta=0
while i<len(palabra):
    print("i es ",i,"la letra es ",palabra[i])
    if palabra[i]!="A" and palabra[i]!="C" and palabra[i]!="T" and palabra[i]!="G":
        cuenta=cuenta+1
        print("secuencia incorrecta")
    i=i+1
if cuenta==0:
    print("secuencia correcta")
    
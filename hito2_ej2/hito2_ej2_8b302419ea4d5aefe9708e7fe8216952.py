palabra = input("Ingresa una palabra:")
palabra = palabra.upper()
print(palabra)
I=0
cuenta=0
while I<len(palabra):
    print("I es",I,"la letra es", palabra[I])
    if palabra[I]=="A" or palabra[I]=="C" or palabra[I]=="T" or palabra[I]=="G":
        cuenta=cuenta+1
        
    I=I+1
if cuenta!=len(palabra):
    print("Secuencia Incorrecta")
else:
    print("Secuencia Correcta")
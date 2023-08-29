cadena = input("Ingrese una cadena\n")
palabra = cadena.lower()
validos = "actg"
x = 0

for i in range(0,len(palabra)):
    elemento = palabra[i]
    
    if not(elemento in validos):
        x -= 1
    else:
        x += 1

if(x == len(palabra)):
    print("Secuencia correcta")
else:
    print("Secuencia Incorrecta")
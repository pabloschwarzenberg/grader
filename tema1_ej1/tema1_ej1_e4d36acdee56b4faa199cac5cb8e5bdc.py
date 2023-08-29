#Suma de los N primeros números
N=int(input("ingrese un numero natural: "))
lasuma=N*(N + 1)/2
if N<=0:
    print(f"no es natural")
else:
    print(f"{lasuma}")
         
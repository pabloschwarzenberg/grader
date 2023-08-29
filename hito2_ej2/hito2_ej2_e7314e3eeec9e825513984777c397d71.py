a=input("Ingrese su seceuncia: ")
i=0
a.lower()
largo=len(a)
for i in range(largo):
    if a[i]=="b" or "d" or "e" or "f" or "h" or "i" or "j" or "k" or "m" or "n" or "l" or "o" or "p" or "q" or "r" or "s" or "u" or "v" or "w" or "x" or "y" or "z":
        print("Secuencia incorrecta")
    else:
        print("Secuencia correcta")

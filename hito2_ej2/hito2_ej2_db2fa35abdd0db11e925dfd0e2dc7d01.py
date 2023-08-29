def vali_secu(x):
    for i in x:
        if i=="a" or i=="A":
            continue
        elif i=="c" or i=="C":
            continue
        elif i=="t" or i=="T":
            continue
        elif i=="g" or i=="G":
            continue
        else:
            return "secuencia incorrecta"
    return "secuencia correcta"

s=str(input("Ingresa un string: "))
print(vali_secu(s))      
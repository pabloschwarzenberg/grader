secuencia=input()

i=0

while i<(len(secuencia)):
    if secuencia[i]==str("a") or secuencia[i]==str("c") or secuencia[i]==str("t") or secuencia[i]==str("g"):
        i=i+1
        if i==(len(secuencia)):
            print("secuencia correcta")
            break
        continue

    else:
        print("secuencia incorrecta")
        break
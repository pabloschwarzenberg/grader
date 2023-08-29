secuencia = str(input("ingrese su secuencia: "))
secuencia.lower()
secuencia1 = list(secuencia)
print(secuencia1)
rec = True
for k in range(len(secuencia1)):
    print(secuencia1)
    print(k)
    print(secuencia1[k])
    print()
    if secuencia1[k] == 'a':
        rec = True
    elif secuencia1[k] == 'c':
        rec = True
    elif secuencia1[k] == 't':
        rec = True
    elif secuencia1[k] == 'g':
        rec = True
    else:
        rec = False
        break
if rec == True:
    print("secuencia correcta")
elif rec == False:
    print("secuencia incorrecta")

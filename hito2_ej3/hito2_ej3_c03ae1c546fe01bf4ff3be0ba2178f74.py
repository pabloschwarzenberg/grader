string = input("Ingrese su string: ")
entero = int(input("Ingrese su entero: "))

string = list(string)
lineas = []
contador = 0
for i in range(0, len(string) - entero + 1):
    string[i] = string[0 + i:entero + i]
del string[len(string) - entero + 1::]
for i in range(0,len(string)):
    contador = 0
    for j in range(0,len(string)):

        if string[i] == string[j]:
            contador += 1
    if contador == 1:
        lineas.append("".join(string[i]))
if lineas == []:
    print("ninguna")
else:
    for i in range(0,len(lineas)):
        print(lineas[i])

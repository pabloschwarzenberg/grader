#Conversión de Decimal a Binario
# Variable

x = input("Ingresa un numero: ")
Numero_binario = []

try:
    x = int(x)
    while True:
        if x%2 == 0:
            x = (x)/2
            x = int(x)
            d = "0"
            Numero_binario.append(d)
            if x == 1:
                d = "1"
                Numero_binario.append(d)
                Numero_binario.append("Resultado=")
                break
            elif x == 0:
                d = "0"
                Numero_binario.append(d)
                Numero_binario.append("Resultado=")
                break
        elif x%2 != 0:
            d = "1"
            x = (x)/2
            x = int(x)
            Numero_binario.append(d)
            if x == 1:
                d = "1"
                Numero_binario.append(d)
                Numero_binario.append("Resultado=")
                break
            elif x == 0:
                d = "0"
                Numero_binario.append(d)
                Numero_binario.append("Resultado=")
                break
    for Numero_binario in Numero_binario[::-1]:
        print(Numero_binario,end='')
except ValueError:
    print("Eso no es un numero.")
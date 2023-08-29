def numero_perfecto(numero):
    suma = 0
    for variable in range(1,numero):
        if numero % variable == 0:
            suma = suma + variable
            
    if numero == suma:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese su número ->"))
    if numero_perfecto(numero):
        print("es un número perfecto",numero)
    else:
        print("no es un número perfecto",numero)          
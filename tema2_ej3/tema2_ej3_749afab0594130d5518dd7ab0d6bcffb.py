def nro_perfecto(numero):
    suma_divisores = 0
    
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
if __name__ == "__main__":
    if suma_divisores == numero:
        return True
    else:
        return False
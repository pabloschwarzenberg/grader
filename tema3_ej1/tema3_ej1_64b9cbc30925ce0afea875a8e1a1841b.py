# completa el código de la función
def suma_divisores(a):
    a = int(a)
    divisores =  []
    suma = 0
    if a == 1:
        return (0,False)
    if a == 2:
        return 0, True
    else:
        for i in range(1, a):
            if a%i == 0:
                divisores.append(i)

    for i in divisores:
        suma = suma + i
    if suma == 1:
        return suma,True
    else:
        return suma, False
if __name__ == "__main__":
  print(suma_divisores(a=input()))
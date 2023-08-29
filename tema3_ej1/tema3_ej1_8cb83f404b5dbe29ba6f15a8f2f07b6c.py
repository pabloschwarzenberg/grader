def suma_divisores(num):
    divisores=0
    if num == 0:
        print("úmero invalido")
    else:
        for i in range(1,num):
            if num%i == 0:
                divisores+=i
    if divisores == 1:
        return divisores, True
    else:
        return divisores, False
if __name__ == "__main__":
    num=int(input("Ingrese su número: "))
    print(suma_divisores(num))
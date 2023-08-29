num = (int(input("Ingrese el numero:")))

def suma_divisores (num):
    dv = [1]

    for i in range(2, num + 1):
        if num % i == 0:
            dv.append(i)


        elif (num % num == 0):
           return False

        else:
           return True

print(suma_divisores(num))
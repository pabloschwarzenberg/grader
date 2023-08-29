def amigos(num1, num2):
    # Sumar los divisores del primer numero
    sumaDivNum1 = 0  # Acumula los divisores del primer numero
    for i in range(1, num1):  # range(1,num1) = [1,2,3,4,5,6,......119]
        if num1 % i == 0:
            # print(i)
            sumaDivNum1 = sumaDivNum1 + i

    # Sumar los divisores del segundo numero
    sumaDivNum2 = 0  # Acumula los divisores del segundo numero
    for i in range(1, num2):  # range(1,num1) = [1,2,3,4,5,6,......283]
        if num2 % i == 0:
            # print(i)
            sumaDivNum2 = sumaDivNum2 + i

    if (sumaDivNum1 == num2 and sumaDivNum2 == num1):
        return True
    else:
        return False
           
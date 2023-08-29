def son_amigos(num1, num2):
    if num1 == num2:
        return False

    sum_divisores_num1 = sum([i for i in range(1, num1) if num1 % i == 0])
    sum_divisores_num2 = sum([i for i in range(1, num2) if num2 % i == 0])

    if sum_divisores_num1 == num2 and sum_divisores_num2 == num1:
        return True
    else:
        return False

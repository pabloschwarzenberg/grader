def amigos(num1,num2):
    sumaDivNum1 = 0  
    for i in range(1, num1):  
        if num1 % i == 0:
            sumaDivNum1 = sumaDivNum1 + i
    sumaDivNum2 = 0  
    for i in range(1, num2):
        if num2 % i == 0:
            sumaDivNum2 = sumaDivNum2 + i
    if (sumaDivNum1 == num2 and sumaDivNum2 == num1):
        return True
    else:
        return False
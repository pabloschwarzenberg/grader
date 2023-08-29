# completa el código de la función
def amigos(num_1,num_2):
    sumaDivNum1 = 0  
    for i in range(1, num_1):  
        if num_1 % i == 0:
            sumaDivNum1 = sumaDivNum1 + i
    sumaDivNum2 = 0  
    for i in range(1, num_2):  
        if num_2 % i == 0:
            sumaDivNum2 = sumaDivNum2 + i
    if (sumaDivNum1 == num_2 and sumaDivNum2 == num_1):
        return True
    else:
        return False
           
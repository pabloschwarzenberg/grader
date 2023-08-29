def Num_Perfecto(num):
    suma = 0
    for i in range(1,num):
        if (num % i == 0):
            suma += i
    if num == suma:
        return False
    else:
        return True
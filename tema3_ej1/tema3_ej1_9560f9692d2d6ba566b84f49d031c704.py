def suma_divisores(a):
    result = 0
    for i in range(1,a):
        if a % i == 0:
            result += i
    if result == 1:
        #print('Es un número primo.')
        return result,True
    else:
        #print('No es un número primo.')
        return result, False
    #return result

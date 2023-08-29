#Condiciones si es True o False
def suma_divisores(a):
    divisores = 0
    for i in range(1, a - 1):
        if a % i != 0:
             continue
        divisores += i
        
    if divisores == 1:
     primo = True
    else:
     primo = False   
    return divisores, primo
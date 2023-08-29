# completa el código de la función
def suma_divisores(a):
    divisores = [1]

    for i in range (2, a +1):
        if  a % i ==0:
            divisores.append(i)
    return sum(divisores)
 
 def es_primo (num):
    contador=0
    for i in range (1,num+1):
        if num % i == 0:
            contador +=1

    if contador == 2:
        return True
    else:
        return False
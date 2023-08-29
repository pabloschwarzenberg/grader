num=int(input('dame un numero decimal: '))
def bina_decimal(num):
    bo = ''
    while num // 2 != 0:
        bo = str(num % 2) + bo
        num = num // 2
    return str(num)+ bo

print('resultado='+str(bina_decimal(num)))
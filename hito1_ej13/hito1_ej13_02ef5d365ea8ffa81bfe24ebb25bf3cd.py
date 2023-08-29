numero = int(input())
esprimo = True

for num in range(2, numero+1):
    if numero % num == 0:
        for num2 in range(2, num):
            if num % num2 == 0:
                esprimo = False
        if esprimo == True:
            print(num)

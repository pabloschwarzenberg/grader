def es_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Write a number: '))
    resultado = es_primo(num)

    if resultado is True:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')


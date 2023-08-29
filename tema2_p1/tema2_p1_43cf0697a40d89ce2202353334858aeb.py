def es_primo(num):
    if num < 1:
        return True
    elif num == 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

def app():
    num = int(input('Write a number: '))
    result = es_primo(num)

    if result is False:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')
if __name__ == '__main__':
    app()

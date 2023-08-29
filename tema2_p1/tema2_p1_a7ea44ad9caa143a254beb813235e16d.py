# por favor escribe aquí tu función
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
    result = es_primo(num)

    if result is True:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    app()
           
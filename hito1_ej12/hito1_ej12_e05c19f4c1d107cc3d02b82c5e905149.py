from random import randint

num_comp = randint(1, 20)

intentos = 5

while intentos != 0:
    num = int(input())
    intentos -= 1

    if num < num_comp:
        print('mi número es mayor')
    elif num > num_comp:
        print('mi número es menor')

    elif num == num_comp:
        intentos = 0

if num == num_comp:
    print('Adivinaste, mi número era {}'.format(num_comp))

else:
    print('No adivinaste, mi número era {}'.format(num_comp))
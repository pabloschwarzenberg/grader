import random
con = 0
n = random.randint(1,20)
print(n)
print(con)

while con < 5:
    m = int(input('Ingrese el numerito: '))
    if m > n:
        print('Es menor')
        con = con + 1
    
    elif m < n:
        print('Es mayor')
        con = con + 1

    elif m == n:
        print('Adivinaste, mi número era {}'.format(n))
        break

if con == 5:
    print('No adivinaste, mi número era {}'.format(n))
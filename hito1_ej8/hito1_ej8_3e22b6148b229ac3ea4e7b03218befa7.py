#Descomponer un número
x = int(input('ingresa un numero de hasta 4 cifras: '))

d1= x%10
d2= x//10%10
d3= x//100%10
d4= x//1000

if 0 <= x < 10:
    print(d1,'U')
else:
    if 10 <= x < 100:
        print(d2, 'D + ', d1, 'U')
    else:
        if 10 <= x < 1000:
            print(d3, 'C + ', d2, 'D + ', d1, 'U')
        else:
            if 1000 <= x < 10000:
                print(d4, 'M + ', d3, 'C + ', d2, 'D + ', d1, 'U')
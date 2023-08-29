#Descomponer un número
num = int(input())
lar = int(len(str(num)))

mil = num//1000
cen = (num-(mil1000))//100
dec = (num- (mil1000 + cen100))//10
uni = unidades=num-(mil1000 + cen100 + dec10)

if lar == 4:
    print(mil, 'M', '+', cen, 'C', '+', dec, 'D', '+', uni, 'U')
elif lar == 3:
    print(cen, 'C', '+', dec, 'D', '+', uni, 'U')
elif lar == 2:
    print(dec, 'D', '+', uni, 'U')
else:
    print(uni, 'U')
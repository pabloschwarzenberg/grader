#Descomponer un número
x=int(input('Ingrese un número de hasta 4 dígitos: '))

u= x%10
d=(x//10)%10
c=(x//100)%10
m=(x//1000)%10

if 0 <= x < 10:
    desc= str(u)+'U'
if 10<= x < 100:
    desc= str(d)+'D +'+str(u)+'U'
if 100<= x <1000:
    desc= str(c)+'C +' +str(d)+'D +'+str(u)+'U'
if 1000<= x < 10000:
    desc= str(m)+'M +'+str(c)+'C +'+str(d)+'D +'+str(u)+'U'

print(desc)
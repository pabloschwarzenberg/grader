#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos: "))
m=numero // 1000
c=(numero //100) % 10
d=(numero//10) % 10
u= numero % 10
if 9999 >= numero >= 1000:
    print(str(m)+'M +',str(c)+'C +',str(d)+'D +',str(u)+'U')
elif 999 >= numero >= 100:
    print(str(c)+'C +',str(d)+'D +',str(u)+'U')
elif 99 >= numero >= 10:
    print(str(d)+'D +',str(u)+'U')
elif 9>= numero >= 1:
    print(str(u)+'U')
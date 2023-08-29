numero = int(input('Ingrese numero para pasar a binario: '))
o = []
while numero > 0:
    r = numero % 2
    numero = int(numero/2)
    o.append(r)
    if numero == 0:
            o.append('resultado=')

for i in reversed(o):
        print(i,end='')
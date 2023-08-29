numero = int(input('ingrese un numero: '))
bin = ""

while(numero>0):
    if(numero%2==0):
        bin= str(0)+bin
    else:
        bin = str(1)+bin
    numero = numero//2
print('resultado=', bin)
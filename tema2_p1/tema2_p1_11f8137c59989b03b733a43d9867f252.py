# por favor escribe aquí tu función
def es_primo(numero):
a=int(input('Número: '))
for i in range(2,a):
    if a%i==0 or a<=1:
        print('False')
        break
    elif a%i!=0 and a>1:
        print('True')           
#Cálculo del dígito verificador de un rut
RUT = input('Ingresar RUT: ')
lista = list(RUT)
serie = [2,3,4,5,6,7,2,3,4,5,6,7]
lista_int = []
for i in lista:
    lista_int.append(eval(i))
base = 0
lista_int.reverse()
for i in range(len(lista_int)):
    base += lista_int[i]*serie[i]
print(base)

resultado = base//11
resultado = base -(11*resultado)
final = 11-resultado

if final == 11:
    print('dv=',0)
elif final == 10:
    print('dv=K')
else:
    print('dv=',final)
      
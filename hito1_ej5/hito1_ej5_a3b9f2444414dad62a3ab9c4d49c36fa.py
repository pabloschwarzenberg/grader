#Cálculo del dígito verificador de un rut
lista = []
otra_lista = []

rut_de_7 = [2,3,4,5,6,7,2]

rut_de_8 = [2,3,4,5,6,7,2,3]

rut =input('Ingrese su rut: ')


for i in reversed(rut):
    lista.append(i)

contador = 0 

if len(lista) == 7:
    for x in rut_de_7:
        producto = int(lista[contador])*int(x)
        contador = contador+1
        otra_lista.append(producto)

        suma_de_productos = sum(otra_lista)

        modulo = suma_de_productos%11

        dv = 11-modulo

    if dv==11:
        print('dv=0')
    elif dv==10:
        print('dv=K')
    else:
        print('dv='+str(dv))
    
        

elif len(lista) == 8:
    for x in rut_de_8:
        producto = int(lista[contador])*int(x)
        contador = contador+1
        otra_lista.append(producto)

        suma_de_productos = sum(otra_lista)

        modulo = suma_de_productos%11

        dv = 11-modulo

    if dv==11:
        print('dv=0')
    elif dv==10:
        print('dv=K')
    else:
        print('dv='+str(dv))
    
              
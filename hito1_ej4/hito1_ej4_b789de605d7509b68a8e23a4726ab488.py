'''Escribe un programa que reciba como entrada un número decimal e imprima el resultado de convertirlo a binario. Por ejemplo, al ingresar el número 33 tu programa debiera imprimir el siguiente mensaje:'''
numero=eval(input('Ingrese un Numero:\t'))
transformacion=(str(bin(numero))).replace('0b','')
print('resultado={}'.format(transformacion))
#Conversión de Decimal a Binario
numero=eval(input('Ingrese un Numero:\t'))
transformacion=(str(bin(numero))).replace('0b','')
print('resultado={}'.format(transformacion))      
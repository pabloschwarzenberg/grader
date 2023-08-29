carga100 = 100
carga50 = 100
carga20 = 100
carga10 = 100
carga5 = 100


def sacar_dinero(cantidad):
global carga100, carga50, carga20, carga10, carga5
if cantidad <= 100 * carga100 + 50 * carga50 + 20 * carga20 + 10 * carga10 + 5 * carga5:
de100 = int(cantidad/100)
cantidad = cantidad % 100
if de100 >= carga100: # y hay suficiebtes billetes de 100
cantidad = cantidad + (de100 - carga100) * 100
de100 = carga100

de50 = int(cantidad / 50)
cantidad = cantidad % 50
if de50 >= carga50: # Si hay suficientes billetes de 50
cantidad = cantidad + (de50 - carga50) * 50
de50 = carga50

de20 = int(cantidad / 20)
cantidad = cantidad % 20
if de20 >= carga20: # y hay suficientes billetes de 20
cantidad = cantidad + (de20 - carga20) * 20
de20 = carga20

de10 = int(cantidad / 10)
cantidad = cantidad % 10
if de10 >= carga10: # y hay suficientes billetes de 10
cantidad = cantidad + (de10 - carga10) * 10
de10 = carga10

de5 = int(cantidad / 5)
cantidad = cantidad % 5
if de5 >= carga5: # y hay suficientes billetes de 5
cantidad = cantidad + (de5 - carga5) * 5
de5 = carga5




# Si todo ha ido bien, la cantidad que resta por entregar es nula:
if cantidad == 0:
# Así que hacemos efectiva la extracción
carga100= carga100 - de100
carga50 = carga50 - de50
carga20 = carga20 - de20
carga10 = carga10 - de10
carga5 = carga5 - de5
return [de100, de50, de20, de10, de5]
else: # Y si no, devolvemos la lista con cinco ceros:
return [0, 0, 0, 0, 0]
else:
return [-1, -1, -1, -1, -1]

try:
c = int(input('Cantidad a extraer: '))
resultado=sacar_dinero(c)
if resultado==[0,0,0,0,0]:
print ('No hay desglose de billetes para su importe')
elif resultado==[-1,-1,-1,-1,-1]:
print ('No hay suficientes billetes')
else:
print ('Billetes de 100', resultado[0])
print ('Billetes de 50:', resultado[1])
print ('Billetes de 20:', resultado[2])
print ('Billetes de 10:', resultado[3])
print ('Billetes de 5:', resultado [4])
except:
print ('Importe incorrecto')
      
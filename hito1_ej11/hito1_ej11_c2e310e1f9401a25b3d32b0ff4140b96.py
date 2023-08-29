#Cajero Automático
carga5000 = 1000
carga20000 = 1000
carga10000 = 1000
 
def sacar_dinero(cantidad):
  global carga5000, carga20000, carga10000
  if cantidad <= 5000 * carga5000 + 20000 * carga20000 + 10000 * carga10000:
 
    de5000 = int(cantidad / 5000)
    cantidad = cantidad % 5000
    if de5000 >= carga5000: # Si hay suficientes billetes de 5000
      cantidad = cantidad + (de5000 - carga5000) * 5000
      de5000 = carga5000
 
    de20000 = int(cantidad / 20000)
    cantidad = cantidad % 20000
    if de20000 >= carga20000: # y hay suficientes billetes de 20000
      cantidad = cantidad + (de20000 - carga20000) * 20000
      de20000 = carga20000
 
    de10000 = int(cantidad / 10000)
    cantidad = cantidad % 10000
    if de10000 >= carga10000: # y hay suficientes billetes de 10000
      cantidad = cantidad + (de10000 - carga10000) * 10000
      de10000 = carga10000
 
    # Si todo ha ido bien, la cantidad que resta por entregar es nula:
    if cantidad == 0:
      # Así que hacemos efectiva la extracción
      carga5000 = carga5000 - de5000
      carga20000 = carga20000 - de20000
      carga10000 = carga10000 - de10000
      return [de5000, de20000, de10000]
    else: # Y si no, devolvemos la lista con cuatro ceros:
      return [0, 0, 0, 0]
  else:
    return [-1, -1, -1, -1]
 
try:
    c = int(input('Cantidad a extraer: '))
    resultado=sacar_dinero(c)
    if resultado==[0,0,0,0]:
        print ('No hay desglose de billetes para su importe')
    elif resultado==[-1,-1,-1,-1]:
        print ('No hay suficientes billetes')
    else:
        print ('Billetes de 5000:', resultado[0])
        print ('Billetes de 20000:', resultado[1])
        print ('Billetes de 10000:', resultado[2])
except:
    print ('Importe incorrecto')
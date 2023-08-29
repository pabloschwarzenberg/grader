#Cajero Automático
usuario_luciano = 10334151
clave_del_usuario_luciano = 1803


saldogg = 100000

saldosuperlol = 1000000

CC = 1
while CC <= 3:
    usuario_del_cajero_luciano = int(input("Ingresa el Usuario, por favor estimado: "))
    clave_del_cajero_luciano= int(input("Ingresa la clave, por favor estimado: "))


    if ((usuario_del_cajero_luciano == usuario_luciano) and (clave_del_cajero_luciano == clave_del_usuario_luciano)):
      CC = 4
    else:

      print("clave invalida")
    if (CC == 3):

        print("tarjeta bloqueada")
        break
    CC = CC +1
    
carga20000 = 20
carga10000 = 40
carga5000 = 40
 
def sacar_dinero(cantidad):
  global carga20000, carga10000, carga5000
  if cantidad <= 20000 * carga20000 + 10000 * carga10000 + 50000 * carga5000:
 
    de20000 = int(cantidad / 20000)
    cantidad = cantidad % 20000
    if de20000 >= carga20000: # billetes de 20000
      cantidad = cantidad + (de20000 - carga20000) * 20000
      de20000 = carga20000
 
    de10000 = int(cantidad / 10000)
    cantidad = cantidad % 10000
    if de10000 >= carga10000: # billetes de 10000
      cantidad = cantidad + (de10000 - carga1000) * 10000
      de10000 = carga10000
 
    de5000 = int(cantidad / 5000)
    cantidad = cantidad % 5000
    if de5000 >= carga5000: #billetes de 5000
      cantidad = cantidad + (de5000 - carga5000) * 5000
      de5000 = carga5000
 
    # ACA SE DESARROLLA!!!
    if cantidad == 0:
      # extracción
      carga20000 = carga20000 - de20000
      carga10000 = carga10000 - de10000
      carga5000 = carga5000 - de5000
      return [de20000, de10000, de5000]
    else: 
      return [0, 0, 0]
  else:
    return [-1, -1, -1]
 
try:
    retiro_del_money = int(input('Cantidad a extraer: '))
    resultado=sacar_dinero(retiro_del_money)
    if resultado==[0,0,0]:
        print ('No hay desglose de billetes para su importe')
    elif resultado==[-1,-1,-1]:
        print ('No hay suficientes billetes')

    else:
        print ('billetes 20000='+str(resultado[0]))
        print ('billetes 10000='+str(resultado[1]))
        print ('billetes 5000='+str(resultado[2]))
except:
    print ('Importe incorrecto')
    

else:
        
         if(retiro_del_money > 100000):
           print("monto excede, no es posible retirar. lo sentimos gg")
         if(retiro_del_money < 0):
           print("monto invalido, no es posible retirar. lo sentimos gg")

         else:
             if((retiro_del_money <= 100000) or (retiro_del_money == 0)):
               print()

resultado_first_luciano= saldogg - retiro_del_money
resultado_two_luciano= saldosuperlol - retiro_del_money


print("saldo cuenta=", resultado_first_luciano, "," "saldo cajero=",resultado_two_luciano)  
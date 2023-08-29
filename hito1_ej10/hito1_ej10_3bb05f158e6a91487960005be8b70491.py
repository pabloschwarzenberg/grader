u = int(input("Ingrese Numero de Usuario: "))
c = int(input("Ingrese Clave: "))
m = 100000
a= 1000000
if (u == 10334151 and c == 1803):
    print("Usuario y clave correto")
    r = int(input("¿Cuanto desea retirar?: "))
    if (r > m):
      print("Monto no permitido")
    else:
      print("Saldo Cuenta= ", m - r)
      print("Saldo Cajero= ",a-r)
else:
    print("Clave declinada")   
input("presione ENTER para finalizar")
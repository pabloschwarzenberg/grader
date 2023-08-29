#Cajero Automático PROFE EN IDLE Y REPLIT SI DA EL CODIGO NOSE PORQUE EN EDEX DA ERROR :C
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
      print("Saldo Cuenta=", m - r)
      print("Saldo Cajero=",a-r)
else:
    print("Clave declinada")
b=r//20000
if(b>=1):
  print("billetes 20000= ",b)
c=(r-((b*20000)))//10000
if(c>=1):
  print("billetes 10000= ",c)
d=(r-((b*20000)+(c*10000)))//5000
if(d>=1):
  print("billetes 5000= ",d)
input("Presione ENTER para finalizar")
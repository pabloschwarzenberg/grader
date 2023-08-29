#Cajero Automático
usuario=int(input("ingrese su nombre de usuario:"))
if usuario==10334151:
    clave=1803
else:print("usuario no registrado")

if usuario==10334151:
    clave=int(input("ingrese una clave:"))
    if clave==1803:
              print("clave valida")
              dinero=int(input("ingrese el monto que desea retirar:"))
              monto=1000000
              monto1=2000 #cantidad de billetes de 20000
              monto2=2000 #cantidad de billetes de 10000
              monto3=4000 #cantidad de billetes de 5000
              monto4=10000 #cantidad de billetes de 1000
              if dinero<monto and dinero%1000==0:
                  m=(dinero//20000)
                  c=((dinero-m*20000)//10000)
                  d=((dinero-m*20000-c*10000)//5000)
                  u=((dinero-m*20000-c*10000-d*5000)//1000)
                  if monto1>m:
                      print(m,"20000")
                  if monto2>c:
                      print(c,"10000")
                  if monto3>d:
                      print(d,"5000")
                  if monto4>u:
                      print(u,"1000")
                      
              else:print("no es valido, ya que el cajero solo entrega billetes de 20000, 10000, 5000 y 1000 o el cajero no posee ese monto")
                  
    else:print("clave invalida")

      
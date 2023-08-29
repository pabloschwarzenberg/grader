#Cajero Automático
usuario=int(input("ingreser usuario: "))
clavereal=1803
claveintento=0
intentos =0
saldocuenta=100000
saldocajero=1000000

while intentos <= 3:
      if intentos > 1:
            claveintento = int(input("clave invalida, intente nuevamente: "))
      else:
            claveintento = int(input("ingrese clave: "))
      intentos += 1
      if claveintento == clavereal:
            monto=int(input("monto que desea retirar: "))
            if monto > saldocuenta:
                print("monto invalido")
            else:
                print("saldo cuenta =",(saldocuenta-monto),",","saldo cajero =",(saldocajero-monto) )
            break
      if intentos == 3:
            print("Tarjeta bloqueada")
            break      
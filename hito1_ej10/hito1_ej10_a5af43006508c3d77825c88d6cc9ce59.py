#Cajero Automático
dinero_cajero = 1000000
dinero_cuenta = 100000
usuario = int(input("usuario: "))
contra = int(input("contraseña: "))
i = 0

if usuario != 10334151 and contra != 1803:
  print("usuario o contraseña inválido")
  while i<=1:
    usuario = int(input("usuario: "))
    contra = int(input("contraseña: "))
    i+=1
    print("usuario o contraseña inválido")
  print("tarjeta bloqueada")
else:
  retiro = int(input("cuanto dinero desea sacar: "))
  if retiro>dinero_cuenta:
    print("monto no permitido")
  else:
    cajero = dinero_cajero-retiro
    cuenta = dinero_cuenta-retiro
    print("saldo cuenta =",cuenta)
    print("saldo cajero =",cajero)
    
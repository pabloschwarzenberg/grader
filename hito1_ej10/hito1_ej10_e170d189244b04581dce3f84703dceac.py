#Cajero Automático
      usuarioEnBD = &
claveEnBD = &
sesion = False
saldo = 100000
iniciar = True

def validarUsuario(usuario, clave) :
  global sesion
  if (usuario == usuarioEnBD and clave == claveEnBD) :
    sesion = True
    return True

  return False

def login() :
  global sesion
  if (sesion) :
    return True

  usuario = input(&#34;Digite usuario: &#34;)
  clave = input(&#34;Digite contraseña: &#34;)
  return validarUsuario(usuario, clave)

def retirar(valor) :
  global saldo
  if (valor &gt; saldo) :
    return False, saldo

  saldo = saldo - valor
  return True, saldo

def depositar(valor) :
  global saldo
  saldo = saldo + valor
  return True, saldo

def consultarSaldo() :
  return True, saldo

def accion(opcion) :
  if (opcion == 1) :
    valor = int(input(&#34;Digite el valor a consignar: &#34;))
    return depositar(valor)
  
  if (opcion == 2) :
    valor = int(input(&#34;Digite el valor a retirar: &#34;))
    return retirar(valor)

  if (opcion == 3) :
    return consultarSaldo()
  
  return False, saldo

def ejecutar() :
  if not login() :
    print(&#34;usuario o contraseña inválido&#34;)
    return

  print(&#34;¿Qué desea hacer?&#34;)
  opcion = int(input(&#34;1 =&gt; Consignar, 2 =&gt; Retirar y 3 =&gt; Consultar saldo: &#34;))
  
  ok, saldo = accion(opcion)
  if not ok :
    print(&#34;No se realizó la acción, saldo:&#34;, saldo)
  else:
    print(&#34;Acción realizada correctamente, saldo:&#34;, saldo)

print(&#34;Bienvenido&#34;)

while (iniciar == True) :
  ejecutar()
  respuesta = input(&#34;¿Deseas realizar otra operación? (SI =&gt; s, si y NO =&gt; valor diferete de s, si): &#34;)
  if (respuesta == &#34;s&#34; or respuesta == &#34;si&#34; or respuesta == &#34;S&#34; or respuesta == &#34;SI&#34;) :
    iniciar = True
  else:
    iniciar = False
    print(&#34;Gracias por utilizar los servicios...&#34;)
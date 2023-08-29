#Cajero Automático
#Detectar variables
 Int usuario
 Int clave
 Int retirar
 Int saldo inicial
 Int calculo1
 Int calculo2
#Solicitar Datos
 Escribir ("Ingrese su número de usuario")
 Leer usuario
 if (usuario existe)
    Escribir ("Bienvenido usuario: ", usuario)
 else if (usuario no existe)  
    Escribir ("El usuario no existe, ingrese nuevamente los datos")
    return 8// Se solicita nuevamnete el usuario, se va a la linea 8
 
 Escribir ("Ingrese su contraseña")
 Leer clave
  if (clave correcta)
     Escribir ("Contraseña correcta, bienvenido usuario: ", usuario)
  else if (clave incorrecta)
     Escribir ("Contraseña inváida, ingrese nuevamente su contraseña")
     return 16// se solicita nuevamente la clave, se va a la linea 16, pero si se ingresa incorrectamnete 3 veces, se bloquea la tarjeta
     if (clave == false 3 times)
      Escribir ("Tarjeta bloqueada")
      Fin // Se saca la tarjeta y se bloquea
     else if (clave == true)
      Escribir ("Ingrese el monto a retirar")
      Leer monto
      if (monto > 100.000)
      Escribir ("Monto no permitido")
      return 27// regresa a la linea 27
      else if (monto <= 100.000)
      Escribir ("Entregando dinero")
 
 #Calcular nuevo saldo de cuenta y de cajero
 calculo 1 = ( 100.000 - monto)
 calculo 2 = ( 1.000.000 - monto)
 
 #Imprimir nuevo saldo de cuenta y de cajero
 Escribir ("Su nuevo saldo de cuenta es: ", calculo1)
 Escribir ("El saldo del cajero actualmente es: ", calculo2)
 Fin // se termina el proceso
 
      
      
  
     

      
  def descomponer_numero(numero):
     unidades = numero % 10
     decenas = (numero // 10) % 10
     centenas = (numero // 100) % 10
     miles = numero // 1000

     descomposicion = ""

       if(miles >0):
        descomposicion = miles,"M "
       if(centenas >0):
        descomposicion = centenas,"C"
       if(decenas >0):
        descomposicion = decenas,"D"
       if(unidades >0):
        descomposicion = unidades,"U"

       return descomposicion.strip()  # Elimina el espacio al final si no hay unidades

 numero = input("Ingrese un número de hasta 4 dígitos: ")
 descomposicion = descomponer_numero(numero)
 print(descomposicion)
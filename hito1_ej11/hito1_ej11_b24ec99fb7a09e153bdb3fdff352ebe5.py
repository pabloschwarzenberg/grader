#Cajero Automático
# Sebastián Zapata
# Obtener dígito verificador de RUTS CHILENOS / CHILEAN ID
# Input: Un numero entero sin guión ni dígito verificador.

# extraerDigitoDesdeDerecha: int int -> int
# Dado un número y una posición, devuelve el digito ubicado en la posición de derecha a izquierda del número.
# Ejemplo: extraerDigitoDesdeDerecha(2015,3) devolverá 0
def extraerDigitoDesdeDerecha(numero, posicion):
   assert type(numero) and type(posicion) == int
   posicion -= 1
   return ((numero//(10**posicion))%10)
# Test
assert extraerDigitoDesdeDerecha(83657,2) == 5

# contarDigitos: int int -> int
# Dado un numero y forzando el segundo parámetro a ser 0, devuelve la cantidad de digitos del primer numero.
# Ejemplo: contarDigitos(44433,0) entrega 5
def contarDigitos(numero, digitos):
   assert type(numero) and type(digitos) == int
   if numero == 0:
      return 0
   elif numero//10 == 0:
      return digitos+1
   else:
      return contarDigitos(numero//10, digitos+1)
# Test
assert contarDigitos(1234567,0)==7

# sumaMultiplicacionDigitos: int int int int -> int
# Dado un rut y los siguientes parámetros forzados a ser 0, 0 y 2 respectivamente, calcula la suma de cada dígito del rut multiplicado por
# cada número de una serie desde el 2 al 7, volviendo al 2 en caso de llegar al final de la serie.
# Ejemplo: sumaMultiplicacionDigitos(20100134, 0, 0, 2) entrega 34
def sumaMultiplicacionDigitos(rut, suma, aux, serie):
   assert type(rut) and type(suma) and type(aux) and type(serie) == int
   if aux==contarDigitos(rut,0):
      return suma
   else:
         if serie==8:
            serie = 2
         suma += extraerDigitoDesdeDerecha(rut, aux+1)*serie
         return sumaMultiplicacionDigitos(rut, suma, aux+1, serie+1)
# Tests
assert sumaMultiplicacionDigitos(20100134, 0, 0, 2) == 34
assert sumaMultiplicacionDigitos(11111111, 0, 0, 2) == 32

# digitoVerificador: int -> str
# Dado un rut entrega su correcto dígito verificador (convertido a texto) dado por el algoritmo de RUT en Chile.
# Ejemplo: digitoVerificador(20100134) entrega "K"
# Ejemplo: digitoVerificador(15641676) entrega "8"
def digitoVerificador(rut):
   suma = sumaMultiplicacionDigitos(rut, 0, 0, 2)
   resto = suma % 11
   verificador = 11 - resto
   if verificador == 11: return str(0)
   elif verificador == 10: return "K"
   else: return str(verificador)
# Tests
assert digitoVerificador(20100134) == "K"
assert digitoVerificador(8205403) == "0"

# consultaDigitoVerificador none -> none
# Establece un diálogo pidiendo un rut en cada entrada e imprimiendo un mensaje con el dígito verificador asociado a ese rut
# si la entrada es 0, dará las gracias y terminará el programa.
def consultaDigitoVerificador():
   rut = int(input())
   if rut != 0:
      print ("El RUT ingresado es: " + str(rut))
      print (u"El dígito verificador es: " + digitoVerificador(rut))      
#Cálculo del dígito verificador de un rut
def extraerDigitoDesdeDerecha(numero, posicion):
   assert type(numero) and type(posicion) == int
   posicion -= 1
   return ((numero//(10**posicion))%10)

assert extraerDigitoDesdeDerecha(83657,2) == 5
def contarDigitos(numero, digitos):
   assert type(numero) and type(digitos) == int
   if numero == 0:
      return 0
   elif numero//10 == 0:
      return digitos+1
   else:
      return contarDigitos(numero//10, digitos+1)
assert contarDigitos(1234567,0)==7
def sumaMultiplicacionDigitos(rut, suma, aux, serie):
   assert type(rut) and type(suma) and type(aux) and type(serie) == int
   if aux==contarDigitos(rut,0):
      return suma
   else:
         if serie==8:
            serie = 2
         suma += extraerDigitoDesdeDerecha(rut, aux+1)*serie
         return sumaMultiplicacionDigitos(rut, suma, aux+1, serie+1)
assert sumaMultiplicacionDigitos(20100134, 0, 0, 2) == 34
assert sumaMultiplicacionDigitos(11111111, 0, 0, 2) == 32
def dv(rut):
   suma = sumaMultiplicacionDigitos(rut, 0, 0, 2)
   resto = suma % 11
   dv = 11 - resto
   if dv == 11: return str(0)
   elif dv == 10: return "K"
   else: return str(dv)
assert dv(20100134) == "K"
assert dv(8205403) == "0"
def consultaDigitoVerificador():
   rut = int(input("Ingrese RUT: "))
   if rut != 0:
      print ("El RUT ingresado es: " + str(rut))
      print (u"El dígito verificador es: " + dv(rut))

consultaDigitoVerificador()   
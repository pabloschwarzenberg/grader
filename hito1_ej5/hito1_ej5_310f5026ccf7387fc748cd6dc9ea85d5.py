print("ingrese el rut sin digito verificador")
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

def digitoVerificador(rut):
   suma = sumaMultiplicacionDigitos(rut, 0, 0, 2)
   resto = suma % 11
   verificador = 11 - resto
   if verificador == 11: return str(0)
   elif verificador == 10: return "K"
   else: return str(verificador)

assert digitoVerificador(20100134) == "K"
assert digitoVerificador(8205403) == "0"

def consultaDigitoVerificador():
   rut = int(input())
   if rut != 0:
      print ("El RUT ingresado es: " + str(rut))
      print (u"dv=" + digitoVerificador(rut)) # Prefiero que se vea feo a no usar tilde jajajaj

consultaDigitoVerificador()


#Cálculo del dígito verificador de un rut
      # codificación=utf-8

# Obtener el dígito verificador del RUT en Python.
#
# La funcion recibe el RUT como un entero,
# y entrega el dígito verificador como un entero.
# Si el resultado es 10, el RUT es "raya k".

del  ciclo de importacion de itertools  

def  digito_verificador ( rut ):
    diitos_invertidos  =  map ( int , invertido ( str ( rut )))
    factores  =  ciclo ( rango ( 2 , 8 ))
    s  =  suma ( d  *  f  para  d , f  en  zip ( digitos_invertidos , factores ))
    retorno ( - s ) %  11
def  ciclo de importación de itertools  

def  digito_verificador ( rut ):
    dígitos_invertidos  =  map ( int , invertido ( str ( rut )))
    factores  =  ciclo ( rango ( 2 , 8 ))
    s  =  suma ( d  *  f  para  d , f  en  zip ( dígitos_invertidos , factores ))
    retorno ( - s ) %  11
def  suma_divisores ( n ):
    suma = 0
    for  i  in  range ( 1 , n ):
        if n  %  i  ==  0 :
            suma += 1
    if  suma  ==  1 :
        return  suma , true
    else :
        return  suma , False
n = int(input ( "Ingrese un número: " ))
es_primo = suma_divisores ( n )
print ("La suma de los divisores de" , n , "es" , s )
if es_primo :
 print ( n , "es primo" )
else :
        print ( n , "no es primo" )

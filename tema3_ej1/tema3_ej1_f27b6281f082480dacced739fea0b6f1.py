def suma_divisores ( n ):

   suma = 0

   para i en rango ( 1 , n ):

       si n % i == 0 :

           suma += yo

   si suma == 1 :

       volver suma , Cierto

   más :

       devolver suma , Falso

 

si __nombre__ == "__principal__" :

   n = int ( entrada ( "Ingrese un número: " ))

   s , es_primo = suma_divisores ( n )

   print ( "La suma de los divisores de" , n , "es" , s )

   si es_primo :
dieciséis
       imprimir ( n , "es primo" )

   más :

       imprimir ( n , "no es primo" ) 
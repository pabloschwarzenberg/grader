#Contestador de celular
nt = int( input( "Ingrese numero telefonico: " ))
hr = int( input( "Ingrese hora de llamada: " ))
if( hr < 8 ):
    print( "CONTESTAR" )
elif( hr < 14 ):
    if( nt - (( nt // 1000 ) *1000 ) == 909 ):
        print( "CONTESTAR" )
    else:
        print( "NO CONTESTAR" )
elif( hr < 17 ):
    print( "NO CONTESTAR" )
elif( 17 <= hr <= 19 ):
    if( ( nt // 100000 ) == 877 ):
        print( "NO CONTESTAR" )
    else:
        print( "CONTESTAR" )
elif( nt > 19 ):
    print( "NO CONTESTAR" )
#Cálculo del dígito verificador de un rut
r = input()
if len( r ) == 8:
    p = ((int(r[0])*8+int(r[1])*9+int(r[2])*4+int(r[3])*5+int(r[4])*6+int(r[5])*7+int(r[6])*8+int(r[7])*9)%11)
    if p < 10:
        print( "dv=" + str( p ) )
    else:
        print( "dv=k" )
if len( r ) == 7:
    p = ((int(r[0])*9+int(r[1])*4+int(r[2])*5+int(r[3])*6+int(r[4])*7+int(r[5])*8+int(r[6])*9)%11)
    if p < 10:
        print( "dv=" + str( p ) )
    else:
        print( "dv=k" )
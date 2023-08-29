numero1=input("ingrese un valor")
numero2=input("ingrese un valor")
numero3=input("ingrese un valor")

if( numero1 <= numero2 <= numero3 ):
    print( numero1 ,",", numero2 ,",", numero3 )
if( numero1 <= numero3 <= numero2 ):
    print( numero1 ,",", numero3 ,",", numero2 )
if( numero2 <= numero1 <= numero3 ):
    print( numero2 ,",", numero1 ,",", numero3 )  
if( numero2 <= numero3 <= numero1 ):
    print( numero2 ,",", numero3 ,",", numero1 )
if( numero3 <= numero1 <= numero2 ):
    print( numero3 ,",", numero1 ,",", numero2 )
if( numero3 <= numero2 <= numero1 ):
    print( numero3 ,",", numero2 ,",", numero1 )
    


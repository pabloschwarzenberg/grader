 import   random
 
animales  = [ 'jabali' ,  'delfin' ,  'guepardo' ,  'elefante' ,  'iguana' ]
largo  =  len ( animales )
indice  =  random . randint ( 0 , largo - 1 )
animal  =  animales [ indice ]
adivinando  = []  #lista con líneas
 
#Mecánica del juego
def   palabraEnLineas ():
     lineas  =  ""
     if   len ( adivinando ) ==  0 :
         for   letra   in   animal :
            adivinando . append ( "_" ) 
    
     for   letra   in   adivinando :
       
         lineas  =  lineas  +  letra  +  " "
    
     print ( lineas )
 
def   existeLetra ( letra , palabra ):
     existe  =  0
     for   i   in   range ( len ( palabra )):
         if   palabra [ i ] ==  letra :
             existe  =  1
             reemplazarLetra ( i , letra ,  adivinando )
     return   existe
 
def   reemplazarLetra ( indice ,  letra ,  lista ):
     lista [ indice ] =  letra
 
def   ganaste ():
     win  =  0
     palabra  =  ""
     for   letra   in   adivinando :
         palabra  =  palabra  + letra
 
     if   animal  ==  palabra :
         win  =  1
 
     return   win
 
errores  =  0
 
print ( f "El animal a adivinar tiene  { largo }  letras" )
 
while   errores  <  5 :
     palabraEnLineas ()
     letra  =  input ( "Ingresa una letra " )
 
     if   existeLetra ( letra ,  animal ) ==  0 :
         errores  =  errores  +  1
         print ( f "Te quedan  { 5 - errores }  oportunidades" )
    
     if   ganaste () ==  1 :
         print ( "Ganaste" )
         break
 
intentos  =  0
if   errores  ==  5 :
         print ( "Desea intentar adivinar el animal" )
         print ( "1 Sí" )
         print ( "2 No" )
         opcion  =  int ( input ())
         if   opcion  ==  1 :
            
             while   intentos  <  3 : 
                 print ( "El animal es" )
                 adivina  =  input ()
                 if   adivina  !=  animal :
                     intentos  =  intentos + 1
                     if   intentos  ==  3 :
                          print ( "Mejor suerte para la próxima" )  
                 else :
                     print ( "Acertaste" )
                     break
         else :
             print ( "Mejor suerte para la próxima" ) 
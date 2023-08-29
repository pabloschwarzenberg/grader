#Descomponer un número
n= int (input( "Ingrese un numero de cuatro dogitos :") )

# requisitos 
if  0<n<10000 :
    print(" Datos ingresados son validos")
else:
    print("Datos ingresados no son validos , solo hasta 4 digitos  ")

u_mil = n//1000
u_centena=(n%1000)//100
u_decenas =((n%1000)% 100) //10
u_unidad =((n%1000)%100)%10 

#salida 
print( u_mil,"M +",u_centena,"C + " ,u_decenas,"D +", u_mil,"U ")       
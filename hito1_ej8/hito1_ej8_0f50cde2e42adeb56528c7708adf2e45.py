numero1=int(input("Ingresar un número que no supere los 4 dígitos:"))
if(numero1>0 and numero1<10000):
 unidad=numero1%10   
 numero2=numero1/10
 decena=numero2%10   
 numero3=numero2/10
 centena=numero3%10   
 miles=numero3/10      

#PRINT 
print(str(int(miles))+"M+"+str(int(centena))+"C+"+str(int(decena))+"D+"+str(int(unidad))+"U")
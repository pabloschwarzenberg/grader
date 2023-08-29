#Ordenar tres números
      ##1_ordenar 3 numero:
#Escribe un programa que reciba tres números y los imprima ordenados de menor
#a mayor, separados por una coma
print("ingresar primer numero")
valor1=int(input())
print("ingresar segundo numero")
valor2=int(input())
print("ingresar tercer numero")
valor3=int(input())
if(valor1<valor2 and valor2<valor3):
    print("",valor1,"-",valor2,"-",valor3)    
if(valor2<valor1 and valor1<valor3):
    print("",valor2,"-",valor1,"-",valor3)    
if(valor3<valor1 and valor1<valor2):
    print("",valor3,"-",valor1,"-",valor2)   
if(valor3<valor2 and valor2<valor1):
    print("",valor3,"-",valor2,"-",valor1)    
if(valor1<valor3 and valor3<valor2):
    print("",valor1,"-",valor3,"-",valor2)  
if(valor2<valor3 and valor3<valor1):
    print("",valor2,"-",valor3,"-",valor1)
else:("Error, los numero son iguales:")
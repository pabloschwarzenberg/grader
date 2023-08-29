#Ordenar tres números
numero1=int(input("numero1:"))
numero2=int(input("numero2:"))
numero3=int(input("numero3:"))
if(numero1<=numero2<=numero3):
    orden1=print(numero1,",",numero2,",",numero3)
if(numero2<=numero1<=numero3):
    orden2=print(numero2,",",numero1,",",numero3)
if(numero2<=numero3<=numero1):
    orden3=print(numero2,",",numero3,",",numero1)
if(numero3<=numero2<=numero1):
    orden4=print(numero3,",",numero2,",",numero1)
if(numero3<=numero1<=numero2):
    orden5=print(numero3,",",numero1,",",numero2)
if(numero1<=numero3<=numero2):
    orden6=print(numero1,",",numero3,",",numero2)
     
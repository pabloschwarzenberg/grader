#Nota final
PT=float(input("Nota de las tareas: "))
PI=float(input("Nota de las interrogaciones: "))
NE=float(input("Nota de los examenes: "))
PP=float(input("Nota de las precentaciones: "))
nota1=(0.3*PT)
nota2=(0.3*PI)
nota3=(0.3*NE)
nota4=(0.1*PP)
resultado=nota1+nota2+nota3+nota4
x=(((resultado-(resultado//1))*100)%10)//1
y=0
resultado=((resultado*10)//1)/10
if x>=5:
    resultado+=0.1       
print(resultado)
          
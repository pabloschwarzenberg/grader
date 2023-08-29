#Descomponer un número
numero=input('ingrese un numero: ')
if len(numero)==4:
    print(numero[0],'M +',numero[1],'C +',numero[2],'D +',numero[3],'U')
elif len(numero)==3:
    print(numero[0],'C +',numero[1],'D +',numero[2],'U')
elif len(numero)==2:
    print(numero[0],'D +',numero[1],'U')
elif len(numero)==1:
    print(nuemro[0],'U')
     
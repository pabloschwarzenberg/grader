#Descomponer un número
      
num = int(input("Introduce el número:"))

unidadmil = num/1000
vas = num%1000
centenas = vas/100
vas = vas%100
decenas = vas / 10
unidades = vas % 10

print("%i" % unidadmil,"M", "+" , "%i" % centenas,"C", "+", " %i" %  decenas,"D" ,"+" , "%i" % unidades,"U" )
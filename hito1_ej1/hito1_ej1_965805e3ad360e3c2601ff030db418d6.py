#Nota Final

nota_1 = input("ingrese la nota: ")
nota_2 = input("ingrese la nota: ")
nota_3 = input("ingrese la nota: ")
nota_4 = input("ingrese la nota: ")

try: 
    nota_1 = float(nota_1) 
    nota_2 = float(nota_2) 
    nota_3 = float(nota_3) 
    nota_4 = float(nota_4) 
    
    nota_final = ((0.3*nota_1)+ (0.3*nota_2)+(0.3*nota_3)+(0.1*nota_4))
    print(nota_final)

except ValueError:
    print("solo se aceptan numeros decimales como notas.")
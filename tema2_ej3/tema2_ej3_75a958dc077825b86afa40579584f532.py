 ##sumar divisores
 for divisor in divisores:
 suma = suma + divisor
 if suma == n:
 esPerfecto = True
 else:
 esPerfecto = False
 return esPerfecto
if __name__=="__main__":
 a=int(input("Ingrese a: "))
 print(numero_perfecto(a))

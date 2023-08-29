 
num_uno = int(input('Introduce el primer número: '))
num_dos = int(input('Introduce el segundo número: '))
num_tres = int(input('Introduce el tercer número: '))
      
Ma = max(num_uno, num_dos, num_tres)
Mi = min(num_uno, num_dos, num_tres)
 
D = (num_uno + num_dos + num_tres) - Ma - Mi
      
print("Los números ordenados de mayor a menor son ", Mi ," , ", D , " , ", Ma)
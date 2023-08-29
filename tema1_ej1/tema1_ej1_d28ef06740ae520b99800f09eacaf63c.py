#Suma de los N primeros números
            
def suma(x):
  N = (x*(x+1))/2
  return N

print ("Suma de los N naturales: \n")
x = int(input("Ingrese numero N a calcular:"))

print (suma(x))
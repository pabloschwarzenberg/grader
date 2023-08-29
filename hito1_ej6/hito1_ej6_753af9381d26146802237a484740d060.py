#Ordenar tres números
print("bienvenida, el programa ordenará de manera ascendente los números que ingreses")
#solicitar los tres números
n1 = int(eval(input("ingresa el primer número: ")))
n2 = int(eval(input("ingresa el segundo número: ")))
n3 = int(eval(input("ingresa el tercer número: ")))

if((n1 <= n2) and (n1 <= n3)):
  menor = n1
  
  if(n2 <= n3):
    medio = n2
    mayor = n3
  else:
    medio = n3
    mayor = n2

elif((n2 <= n1) and (n2 < n3)):
  menor = n2
  
  if(n1 <= n3):
    medio = n1
    mayor = n3
  else:
    medio = n3
    mayor = n1
    
else:
  menor = n3
  
  if(n1 <= n2):
    medio = n1
    mayor = n2
  else:
    medio = n2
    
#Mostrar los números ordenados y finalizar el programa
print("los números ordenados son: ", menor,",", medio,",", mayor)
print("fin del programa")
#Números perfectos
def numero_perfecto(x):
    s = 0
    for i in range(1,x):
      if x%i == 0:
          s+=i
    if s == x:
      return True
    else:
       return False

if __name__ =="main_":
    x=int(input("Ingrese entero: "))
    print(numero_perfecto(x))
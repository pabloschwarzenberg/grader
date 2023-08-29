def jerigonzo(string):
    return string

if __name__ == "_main_":
    pass
def numero_perfecto(a):
    suma = 0
    for i in range(1,a):
      if a%i == 0:
          suma+=i
    if suma == a:
      return True
    else:
       return False

if __name__ =="main":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
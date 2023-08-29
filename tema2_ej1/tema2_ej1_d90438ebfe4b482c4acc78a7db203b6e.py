import math

def area_rectangulo(base,altura):
    resultado = base * altura
    return resultado

def area_triangulo(base,altura):
    resultado = ( base * altura ) / 2
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado = (1/2) * diagonal1 * diagonal2
    return resultado
    
def area_circulo(radio):
    resultado = math.pi * (radio)**2
    return resultado

if __name__ == "__main__":
  
  Var_1 = eval(input())
  Var_2 = eval(input())
  area_rectangulo(Var_1 , Var_2)
  Var_3 = eval(input())
  Var_4 = eval(input())
  area_triangulo(Var_3 , Var_4)
  Var_5 = eval(input())
  Var_6 = eval(input())
  area_rombo(Var_5 , Var_6)
  Var_7 = eval(input())
  area_circulo(Var_7)
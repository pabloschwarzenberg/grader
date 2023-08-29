import math

def area_rectangulo(a,b):
    area = a * b 
    return area

def area_triangulo(c,d):
    area2 = c * d / 2 
    return area2 
   
def area_rombo(e,f):
    area3 = (e * f) / 2  
    return area3

def area_circulo(g):
    ar = math.pi * (g * g)
    return ar

if __name__ == "__main__":
    input_a = float(input("inserte base: "))
    input_b = float(input("inserte altura: "))
    print("area", area_rectangulo(input_a, input_b))
    
    input_c = float(input("inserte base: "))
    input_d = float(input("inserte altura: "))
    print("area2", area_triangulo(input_c, input_d))
    
    input_e = float(input("inserte lado: "))
    input_f = float(input("inserte angulo: "))
    print("area3", area_rombo(input_e, input_f))
    
    input_g = float(input("inserte radio: "))
    print("ar", area_circulo(input_g))
      
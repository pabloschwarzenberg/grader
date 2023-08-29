# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:59:48 2016

@author: Nicolás
"""
import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return(area)

def area_rectangulo(base,altura):
    area=base*altura
    return(area)

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return(area)

def area_circulo(radio):
    area=math.pi*(radio**2)
    return(area)
    
if __name__ == "__main__":
  while True:
      print("""Menú Calculadora Geométrica:
      1.Calcular área de triángulo
      2.Calcular área de rectángulo
      3.Calcular área de rombo
      4.Calcular área de circulo""")
      sel=int(input("Ingrese el número de su elección: "))
      if sel==1:
          a=eval(input("Ingrese base del triángulo: "))
          b=eval(input("Ingrese altura del triángulo: "))
          area=area_triangulo(a,b)
          print("El área del triángulo es",area,".")
      elif sel==2:
          a=eval(input("Ingrese base del rectángulo: "))
          b=eval(input("Ingrese altura del rectángulo: "))
          area=area_rectangulo(a,b)
          print("El área del rectángulo es",area,".")
      elif sel==3:
          a=eval(input("Ingrese diagonal 1 del rombo: "))
          b=eval(input("Ingrese diagonal 2 del rombo: "))
          area=area_rombo(a,b)
          print("El área del rombo es",area,".")
      elif sel==4:
          a=eval(input("Ingrese radio del círculo: "))
          area=area_circulo(a)
          print("El área del circulo es",area,".")
      else:
          print("Opción inválida. El programa se reiniciará.")
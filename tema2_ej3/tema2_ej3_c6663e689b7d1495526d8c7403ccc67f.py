# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:26:23 2016

@author: Nicolás
"""

def numero_perfecto(a):
    divs=[]
    for i in range(1,a):
        if a%i==0:
            divs.append(i)
    if sum(divs)==a:
        return(True)
    else:
        return(False)
if __name__ == "__main__":
  print("Este programa calcula la suma de números perfectos en el rango [1,n],\nsiendo n el número ingresado por el usuario.")
  n=int(input("Ingrese n: "))
  perfs=[]
  for i in range(1,n+1):
      if numero_perfecto(i):
          perfs.append(i)
  print("Los números perfectos en el rango ingresado son",perfs,"y sumados dan\ncomo resultado",sum(perfs),".")
    
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:33:53 2016

@author: Nicolás Rodríguez
"""

def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    output=[]    
    for i in range(0,len(palabra)):
        if palabra[i].isupper():
            letra=palabra[i].lower()
            print(letra)
            pos=alfabeto.find(letra)
            letra=alfabeto[pos+13]
            letra=letra.upper()
            print(letra)
            output.append(letra)
            print(output)
        else:
            letra=palabra[i]
            print(letra)
            pos=alfabeto.find(letra)
            letra=alfabeto[pos+13]
            print(letra)
            output.append(letra)
            print(output)
    print(output)
    output="".join(output)
    return(output)
                

if __name__=="__main__":
    inp=input("Ingresa la palabra que quieras encriptar: ")
    res=rot13(inp)
    print("El resultado es: ",res)

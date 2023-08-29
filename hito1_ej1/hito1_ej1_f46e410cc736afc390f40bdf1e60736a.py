#Nota final
from tkinter import *
 
def addNumbers():
    n1=float(cTexto1.get())*(0.20)
    n2=float(cTexto2.get())*(0.20)
    n3=float(cTexto3.get())*(0.20)
    n4=float(cTexto4.get())*(0.20)
   
    
    res=(n1)+(n2)+(n3)+(n4)
    myText.set(res)
    

  
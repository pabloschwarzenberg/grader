#Sistema de Ecuacionesfrom ast import Num
import math

n1 = int(input('1er numero: '))
n2 = int(input('2do numero: '))
n3 = int(input('3er numero: '))
n4 = int(input('4to numero: '))
n5 = int(input('5to numero: '))
n6 = int(input('6to numero: '))
print(n1,"x ","+ ",n2, "y ","= ",n3)
print(n4,"x ","+ ",n5, "y ","= ",n6)

def despejeYX(n1, n2, n3, n4, n5, n6):
    w = (n3 - n2)/n1
    y = (n1*n6 - n3*n4)/(n5*n1 - n2*n4)
    x = (n3 - n2*y)/n1
    print("x","=",x)
    print("y","=",y)

despejeYX(n1, n2, n3, n4, n5, n6)      
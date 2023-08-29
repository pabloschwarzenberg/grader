#Descomponer un número
numero=int(input())
d1=numero//1000
numero-=d1*1000
d2=numero//100
numero-=d2*100
d3=numero//10
numero-=d3*10
d4=numero
print("{0}M + {1}C + {2}D + {3}U".format(d1,d2,d3,d4))
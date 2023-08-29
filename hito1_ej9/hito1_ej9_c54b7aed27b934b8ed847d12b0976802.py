#ec_1=input("ingrese la primera ecuacion: ")
#ec_2=input("ingrese la segunda ecuacion: ")
#def comprobar(st,n):
#    if ("")==st[0]:
#        n=1
#    else:
#        n=int(st[0])
#    return n    
a=int(input())        
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
#ec_1=ec_1.split("x")
#a=comprobar(ec_1,a)
#del ec_1[0]
#ec_1=ec_1[0]
#ec_1=ec_1.split("y")
#b=comprobar(ec_1,b)
#del ec_1[0]
#ec_1=ec_1[0]
#ec_1=ec_1.split("=")
#c=int(ec_1[1])

#ec_2=ec_2.split("x")
#d=comprobar(ec_2,d)
#del ec_2[0]
#ec_2=ec_2[0]
#ec_2=ec_2.split("y")
#e=comprobar(ec_2,e)
#del ec_2[0]
#ec_2=ec_2[0]
#ec_2=ec_2.split("=")
#f=int(ec_2[1])
x=((b*f)-(e*c))/((b*d)-(a*e))
y=((a*f)-(d*c))/((a*e)-(d*b))
print ("x="+str(round(x,1)))
print ("y="+str(round(y,1)))
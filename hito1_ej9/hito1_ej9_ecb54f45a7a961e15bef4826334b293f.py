#Sistema de Ecuaciones
def sist(a,b,c,d,e,f):
     g=a*e-b*d
     h=b*d-a*e
     if g==0 or h==0:
          print("No se puede resolver")
          return False
     else: 
          x = round((c * e - b * f) / g,1)
          y = round((c * d - a * f) / h,1)
          print("'x=",x,"'","'y=",y,"'")
          return(x,y)
i=sist(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))
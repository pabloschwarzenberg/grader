#Sistema de Ecuaciones
      
      
def sistemaEcuaciones(a,b,c,d,e,f):
    existeFuncion = a*e - b*d
    #asd = existeFuncion
    #print(asd)
    if existeFuncion != 0:
        x = (c*e - b*f)/ existeFuncion
        y = (a*f - c*d)/ existeFuncion
        #print(x)
        #print(y)
        #return
        print("['X={}']".format(x))
        print("['Y={}']".format(y))

        #return x, y
    else:
        print("Error")
        #return none, none

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
d = int(input("Ingrese el cuarto numero: "))
e = int(input("Ingrese el quinto numero: "))
f = int(input("Ingrese el sexto numero: "))

#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
#print(f)

print(sistemaEcuaciones(a, b, c, d, e, f))
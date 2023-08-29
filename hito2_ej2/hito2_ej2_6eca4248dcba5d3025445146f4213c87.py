a=input("Ingrese secuencia:")
i=0

while i<len(a):
        if a[i]!="a" and a[i]!="A" and a[i]!="c" and a[i]!="C" and a[i]!="t" and a[i]!="T" and a[i]!="g" and a[i]!="G":
            print("La secuencia",a,"es incorrecta")
        
        else:
            print("La secuencia",a,"es correcta")
        
        i=i+1
     
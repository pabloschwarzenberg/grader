def solucion_ecu(a,b,c,d,e,f):
    DE= (a*e-b*d)
    if DE != 0:
        X= (c*e-b*f)/DE
        Y= (a*f-c*d)/DE
        return X,Y
    else:
        return nada,nada
print("digite valores para a,b,c,d,e,f: ")
a,b,c,d,e,f= map(float,input().split())

print(solucion_ecu(a,b,c,d,e,f))
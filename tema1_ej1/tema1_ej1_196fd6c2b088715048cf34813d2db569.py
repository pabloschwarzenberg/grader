lista=[]
cannat = int(input("ingrese cantidad de naturales: "))
for i in range(cannat):
    lista.append(int(input("ingresar numero %d: "%i)))
    print("resultado es %f " %(i*(i+1)/2))

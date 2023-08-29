#Conversión de Decimal a Binario
def b(de):
    bi=''
    while de//2!=0:
        bi=str(de%2)+bi
        de=de//2
    return str(de)+bi
e=int(input("Ingrese el numero:"))
print("resultado=",b(e))
    

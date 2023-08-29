#Cálculo del dígito verificador de un rut
def dig(num):
    ini=num
    conta=2
    suma=0
    while num>0:
        suma= suma + (conta * (num%10))
        conta=conta+1
        if conta==8:
            conta=2		
        num=num/10
    conta=suma%11
    valor=11-conta
    if valor==10:
        valor="K"	
    if valor==11:
        valor="0"
    return "%s-%s"%(ini,valor)
#Cálculo del dígito verificador de un rut
d=sum([int(n)*(i%6+2)for i,n in enumerate(raw_input()[::-1])])%11
print'K'if(d==1)else 11-d
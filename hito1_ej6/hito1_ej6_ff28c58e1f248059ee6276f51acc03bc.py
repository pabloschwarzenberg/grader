#Ordenar tres números
a = int(input("escriba un numero : "))
b = int(input("escriba otro numero : "))
c = int(input("escriba otro numero : "))

suma = (a + b + c)

mayor = max( a , b , c )
menor = min( a , b , c )
m = (mayor - menor)
medio =  suma - mayor - menor
print (" el oden de menor a mayor es : " , menor , "," ,  medio , "," , mayor)

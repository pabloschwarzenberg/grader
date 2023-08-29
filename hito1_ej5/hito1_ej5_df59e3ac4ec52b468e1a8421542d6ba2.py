primdig=int(input("Ingrese el 1er digito de su rut: "))
seconddigito=int(input("Ingrese el 2do digito de su rut"))
terdig=int(input("Ingrese el 3er digito de su rut: "))
cuardig=int(input("Ingrese el 4to digito de su rut: "))
quindig=int(input("Ingrese el 5to digito de su rut: "))
sextodig=int(input("Ingrese el 6to digito de su rut: "))
septdig=int(input("Ingrese el 7mo digito de su rut: "))
octadig=int(input("Ingrese el 8vo digito de su rut: "))
pr=primdig*2
sr=seconddigito*3
tr=terdig*4
cr=cuardig*5
qr=quindig*6
sextor=sextodig*7
septr=septdig*2
octar=octadig*3
firstecua=pr+sr+tr+cr+qr+sextor+septr+octar
secondecua=(firstecua/11)
tercerecua=round(secondecua,0)
cuarecua=11*tercerecua
quintecua=firstecua-cuarecua
sextecua=11-quintecua
ultimate= int(sextecua)
if(sextecua==11):
    print("Su digito verificador es: 0")
if(sextecua==10):
    print("Su digito verificador es: K")
print("Su digito verificador es",ultimate)
#Aprobación de créditos
I= int(input('introdusca sus ingresos: ')) #ingresos
an= int(input('introdusca su año de nacimiento: '))#año nacimiento
nh= int(input('introdusca su numero de hijos: ')) #numero de hijos
apb= int(input('introdusca cuantos años tiene de pertenencia al banco: ')) #años pertenencia al banco
ec= input('introduca su estado civil:\nS: si es soltero \nC: si es casado \n:') #estado civil
cc= input('introdusca donde vive\nU: si es urbano\nR: si es rural \n:') #ciudad o campo

C=1
S=2

U=3
R=4

e= 2022 - an #edad

if apb > 10 and nh >= 2:
    print('APROBADO')
elif ec == 1 and nh > 3 and 45<e and e<55:
    print('APROBADO')
elif I > (25*10**4) and ec == 2 and cc == 3:
    print('APROBADO')
elif (35*10**4)< I and apb> 5:
    print('APROBADO')
elif cc == 4 and ec == 1 and nh<2:
    print('APROBADO')

else:
    print('RECHAZADO')
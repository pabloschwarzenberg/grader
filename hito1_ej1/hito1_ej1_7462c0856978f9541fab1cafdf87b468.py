#Nota final
pt=eval(input('nota tareas: '))
pi=eval(input('nota interrogaciones; '))
ne=eval(input('nota examen: '))
pp=eval(input('nota presentacion'))
nf=((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp))
nfd=round(nf,1)
print('resultado :',round(nfd,2))
#Nota final
tar_ = float(input('ingrese su nota de tareas                  '))
int_ = float(input('ingrese su nota de la interrogacion        '))
exa_ = float(input('ingrese su nota de la examen               '))
pre_ = float(input('ingrese su nota de presentacion            '))
promedio=((tar_*0.3)+(int_*0.3)+(exa_*0.3)+(pre_*0.1))
print (round(promedio,1))
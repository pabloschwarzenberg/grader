#Nota final con float : Decimales.
PT = int and float(input("Por favor ingrese su nota de Tareas - Equivalente a un 30%: "))
PI = int and float(input("Por favor ingrese su nota de Interrogaciones - Equivalente a un  30%: "))
NE = int and float(input("Por favor ingrese su nota de Examen - Equivalente a un 30%: "))
PP = int and float(input("Por favor ingrese su nota de Presentación - Equivalente a un 10%: "))

nota_pt = PT*0.3
nota_pi = PI*0.3
nota_ne = NE*0.3
nota_pp = PP*0.1

#Acá se realiza el cáculo
nota_promedio = PT + PI + NE + PP
nota_ponderada = nota_pt + nota_pi + nota_ne + nota_pp
nota_final = nota_promedio / nota_ponderada

#El resultado de la variable y la tomo y la dejo con un decimales
calculo = round(nota_final,1)
print('El promedio: ', calculo)
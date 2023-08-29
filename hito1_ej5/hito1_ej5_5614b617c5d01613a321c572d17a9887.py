#Cálculo del dígito verificador de un rut
rut_sin_validador = eval(input("ingrese su rut sin digito verificador y sin puntos: "))
n1 = (rut_sin_validador%1000000000 // 10000000)
n2 = (rut_sin_validador%10000000 // 1000000)
n3 = (rut_sin_validador%1000000 // 100000)
n4 = (rut_sin_validador%100000 // 10000)
n5 = (rut_sin_validador%10000 // 1000)
n6 = (rut_sin_validador%1000 // 100)
n7 = (rut_sin_validador%100 // 10)
n8 = (rut_sin_validador%10)

formula_digito_v1 = (n8 * 2) +(n7 * 3)+(n6 * 4)+(n5 * 5)+(n4 * 6)+(n3 * 7)+(n2 * 2)+(n1 * 3) 
formula_digito_v2 = formula_digito_v1 // 11
formula_digito_v3 = (formula_digito_v1) - (11 * formula_digito_v2)
formula_final = (11) - (formula_digito_v3)
if (formula_final == 11):
  print("su dv=0")
elif (formula_final == 10):
  print("su dv=k")
else:  
  print("su dv=", formula_final)
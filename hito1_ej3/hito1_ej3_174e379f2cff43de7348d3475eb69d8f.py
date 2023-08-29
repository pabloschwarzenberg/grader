import os, sys

salario = float (input ('Ingresa el valor de salario: '))
print ('Selecciona el valor de reportado en la central de riesgos.')
print ('\t1.- Si')
print ('\t2.- No')
sys.stdout.write ('\t')
reportado_en_la_central_de_riesgos = 0
while reportado_en_la_central_de_riesgos<1 or reportado_en_la_central_de_riesgos>2:
    reportado_en_la_central_de_riesgos = int (input (': '))
    if reportado_en_la_central_de_riesgos<1 or reportado_en_la_central_de_riesgos>2:
        sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
print ('Selecciona el valor de creditos en otros bancos.')
print ('\t1.- Si')
print ('\t2.- No')
sys.stdout.write ('\t')
creditos_en_otros_bancos = 0
while creditos_en_otros_bancos<1 or creditos_en_otros_bancos>2:
    creditos_en_otros_bancos = int (input (': '))
    if creditos_en_otros_bancos<1 or creditos_en_otros_bancos>2:
        sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
if salario>120000 and reportado_en_la_central_de_riesgos==2 and creditos_en_otros_bancos==2:
    credito=salario*5
    print ('Cr\u00E9dito aprobado.')
else:
    credito=0
    print ('No cumple con las condiciones para el pr\u00E9stamo.')
print ('Valor de credito: ' + repr (credito))
print ()
os.system ('pause')
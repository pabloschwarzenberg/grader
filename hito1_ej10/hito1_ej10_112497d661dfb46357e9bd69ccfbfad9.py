#Cajero Automático
input:"Ingrese su usuario"
print: (int)"---------------",int:10334151
input:"Ingrese su clave de usuario"
print: (int)"---------------",int:1803
if: "clave no corresponde" print: "clave inválida"
input: (int)"---------------"
input: (int)"---------------"
input: (int)"---------------"
if: "Es 3 veces inválida" print: "tarjeta bloqueada"
if: "clave es válida" print:"monto a retirar"
input: (int) "--------------"
if: "monto no es válido" print: "monto no permitido"
if: "monto es válido" print: "monto a retirar"
input: (int) "---------------"

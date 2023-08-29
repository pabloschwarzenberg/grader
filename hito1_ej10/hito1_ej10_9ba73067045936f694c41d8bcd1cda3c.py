#Cajero Automático
  Inicio
 var:x=entero ,saldo cajero: 1.000.000, saldo cuenta: 100.000
"ingresar nombre de usuario y clave para continuar";
si (nombre de usuario=10334151, clave=1803 )
(clave valida)
"introducir monto a retirar", x; entonces{                                                
si (al retirar monto x, descontarle ese  valor x al cajero y a la cuenta)                 
}                                                                                                                                                                                
imprimir: saldo cajero= 1.000.000-x, saldo cuenta=100.000-x (invalida)                     
                                                                                                                                                                           


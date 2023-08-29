#Cálculo del dígito verificador de un rut
   rut = InputBox("Ingrese RUT sin digito ni puntos", "busca digito")
x = Len(rut)
a = 0: m = 2
For c = x To 1 Step -1
If m > 7 Then
m = 2
End If
a = a + Mid(rut, c, 1) * m
m = m + 1
Next c
a = Round(11 - (((a / 11) - Int(a / 11)) * 11))
If a = 10 Then
a = "K"
End If
If a = 11 Then
a = "0"
End If
Cells(2, 2) = rut & "-" & a   
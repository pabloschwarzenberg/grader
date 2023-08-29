#Cálculo del dígito verificador de un rut
int main() {
    int rut, suma = 0, multiplicador = 1, digito_verificador;

    cout << "Ingrese el rut sin dígito verificador: ";
    cin >> rut;

    // Invertimos el orden del rut
    while (rut != 0) {
        multiplicador++;
        suma += (rut % 10) * multiplicador;
        rut /= 10;
        if (multiplicador == 7) {
            multiplicador = 1;
        }
    }

    // Calculamos el dígito verificador
    digito_verificador = 11 - (suma % 11);

    // Impresión del resultado
    if (digito_verificador == 10) {
        cout << "dv=k\n";
    } else if (digito_verificador == 11) {
        cout << "dv=0\n";
    } else {
        cout << "dv=" << digito_verificador << endl;
    }

    return 0;
}
```      
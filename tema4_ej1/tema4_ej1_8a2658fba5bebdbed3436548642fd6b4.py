if intentos > 0 :
        print("Palabra oculta:", palabra_oculta)
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(entrada) == 1:
            if entrada in palabra_secreta:
                palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, entrada)
                if palabra_oculta == palabra_secreta:
                    print("¡Adivinaste la palabra! Felicitaciones.")
                    break
                else:
                    print("¡Letra encontrada!")
            else:
                print("Letra incorrecta.")
                intentos -= 1
        elif len(entrada) == len(palabra_secreta):
            if entrada == palabra_secreta:
                print("¡Adivinaste la palabra! Felicitaciones.")
                break
            else:
                print("Palabra incorrecta.")
                intentos -= 1
        else:
            print("Entrada inválida. Debes ingresar una letra o la palabra completa.")

        if intentos == 0:
            print("¡Se te acabaron los intentos!")
            print("La palabra secreta era:", palabra_secreta)
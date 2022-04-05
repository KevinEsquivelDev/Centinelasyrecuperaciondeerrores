import re


def if_integer(string):
    reg_exp = "[-+]?\d+$"
    return re.match(reg_exp, string) is not None


def menu():
    val = True
    while val is True:
        try:
            print("Calculadora básica")

            print("1. Opción Sumar")

            print("2. Opción Restar")

            print("3. Opción Multiplicar")

            print("4. Opción Dividir")

            print("Precione cualquier numero para salir")

            opcion = int(input("\nSeleccione una opción del 1 al 4: "))

            if opcion == 1:
                escape = "s"
                total = "0"

                print("\nEjecutando la opción Sumar")

                while escape == "s":

                    try:
                        print("Para dejar de sumar presione la letra (s)")
                        suma = input("\nEscriba un  numero: ")

                        int(suma)
                        total = float(total) + float(suma)
                        print("El total actual de la suma es: ", float(total))
                    except ValueError:
                        if suma == "s":
                            escape = "n"
                        else:
                            print("Oops! xD este caracter no se puede sumar")

                print("El total de la suma es: ", float(total))


            elif opcion == 2:

                escape = "s"
                total = "0"

                print("\nEjecutando la opción restar")

                while escape == "s":

                    try:
                        print("Para dejar de restar presione la letra (s)")
                        resta = input("\nEscriba un  numero: ")

                        int(resta)

                        if total == "0":
                            total = resta
                        else:
                            total = float(total) - float(resta)
                        print("El total actual de la resta es: ", float(total))
                    except ValueError:
                        if resta == "s":
                            escape = "n"
                        else:
                            print("Oops! xD este caracter no se puede resta")

                print("El total de la resta es: ", float(total))
                print("\n")


            elif opcion == 3:

                escape = "s"
                total = "0"

                print("\nEjecutando la opción Multiplicar")

                while escape == "s":

                    try:
                        print("Para dejar de Multiplicar presione la letra (s)")
                        Multiplicar = input("\nEscriba un  numero: ")

                        int(Multiplicar)

                        if total == "0":
                            total = Multiplicar
                        else:
                            total = float(total) * float(Multiplicar)
                        print("El total actual de la Multiplicación es: ", float(total))
                    except ValueError:
                        if Multiplicar == "s":
                            escape = "n"
                        else:
                            print("Oops! xD este caracter no se puede Multiplicar")

                print("El total de la Multiplicación es: ", float(total))
                print("\n")

            elif opcion == 4:

                escape = "s"
                total = "0"

                print("\nEjecutando la opción Dividir")

                while escape == "s":

                    try:
                        print("Para dejar de Dividir presione la letra (s)")
                        Dividir = input("\nEscriba un  numero: ")

                        int(Dividir)

                        if total == "0":
                            total = Dividir
                        else:
                            if Dividir == "0":
                                print("\nNo se puede dividir dentro de 0")
                            else:
                                total = float(total) / float(Dividir)
                        print("El total actual de la Dividición es: ", float(total))
                    except ValueError:
                        if Dividir == "s":
                            escape = "n"
                        else:
                            print("Oops! xD este caracter no se puede Dividir")

                print("El total de la Dividición es: ", float(total))
                print("\n")

            else:
                print("Saliendo...")
                val = False

        except ValueError:
            print("\nOops! xD ocurrió un error")
            print("\n")


menu()

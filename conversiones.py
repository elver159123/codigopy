def convertir_a_binario(numero, base):
    if base == 10:
        return bin(numero)[2:]
    elif base == 8:
        return oct(numero)[2:]
    elif base == 16:
        return hex(numero)[2:]
    elif base == 2:
        return str(numero)

def mostrar_tabla(numeros):
    print("\nTabla de conversiones:")
    print("+------------+------------+------------+------------+")
    print("| Decimal    | Binario    | Octal      | Hexadecimal|")
    print("+------------+------------+------------+------------+")
    for num in numeros:
        decimal = num[0]
        binario = num[1]
        octal = num[2]
        hexadecimal = num[3]
        print(f"| {decimal:<10} | {binario:<10} | {octal:<10} | {hexadecimal:<10} |")
    print("+------------+------------+------------+------------+")

def principal():
    numeros = []
    while True:
        try:
            numero = input("\nIngresa un número (o 'salir' para terminar): ")
            if numero.lower() == "salir":
                break

            base = int(input("Selecciona la base (2, 8, 10, 16): "))
            if base not in [2, 8, 10, 16]:
                print("Base no válida. Debe ser 2, 8, 10 o 16.")
                continue

            numero_decimal = int(numero, base)
            salida_binaria = convertir_a_binario(numero_decimal, 10)
            salida_octal = convertir_a_binario(numero_decimal, 8)
            salida_hexadecimal = convertir_a_binario(numero_decimal, 16)

            numeros.append((numero_decimal, salida_binaria, salida_octal, salida_hexadecimal))
        except ValueError:
            print("Ingresa un número válido.")

    mostrar_tabla(numeros)

if __name__ == "__main__":
    principal()
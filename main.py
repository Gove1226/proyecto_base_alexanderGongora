from clases.avanzadas import CalculadoraAvanzada

def main():
    while True:
        print("--- Calculadora ---")
        print("1. Potencia")
        print("2. Raíz cuadrada")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            print(f"Resultado: {CalculadoraAvanzada.potencia(base, exponente)}")

        elif opcion == "2":
            numero = float(input("Ingresa el número: "))
            print(f"Resultado: {CalculadoraAvanzada.raiz_cuadrada(numero)}")

        elif opcion == "3":
            print("Saliendo de la calculadora...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
    
    
    

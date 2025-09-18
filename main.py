def main():
  print("Hello learners!")

if __name__=="__main__":
  main()
  def addmultiplenumbers(numbers):
    """Suma todos los números de la lista"""
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    """Multiplica todos los números de la lista"""
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    """Devuelve True si num es par, False si no"""
    return num % 2 == 0

def isitaninteger(num):
    """Devuelve True si num es un número entero, False si no"""
    return isinstance(num, int)

def main():
    print("Hello learners!")
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Saber si un número es par")
        print("4. Saber si un número es entero")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nums = input("Escribe números separados por espacio: ")
            lista = [float(x) for x in nums.split()]
            print("Resultado de la suma:", addmultiplenumbers(lista))

        elif opcion == "2":
            nums = input("Escribe números separados por espacio: ")
            lista = [float(x) for x in nums.split()]
            print("Resultado de la multiplicación:", multiplymultiplenumbers(lista))

        elif opcion == "3":
            n = float(input("Escribe un número: "))
            print("¿Es par?:", isiteven(n))

        elif opcion == "4":
            n = float(input("Escribe un número: "))
            print("¿Es entero?:", isitaninteger(n))

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

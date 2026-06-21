# calculadora_operaciones_v1.py
 
print("=== BIENVENIDO A LA CALCULADORA V1 ===")
 
# Pedimos el primer número fuera del bucle (solo se pide la primera vez)

try:

    num1 = float(input("Introduce el primer número: "))

except ValueError:

    print("Eso no es un número válido. Reinicia la aplicación.")

    exit()
 
while True:

    # 1. Pedir la operación y convertirla a minúsculas

    operacion = input("Introduce la operación (suma, resta, multiplicacion, division) o 'FIN' para salir: ").lower()

    # Comprobar si el usuario quiere salir

    if operacion == "fin":

        print("¡Gracias por usar la calculadora! Fin del programa.")

        break

    # Validar si la operación es correcta

    if operacion not in ["suma", "resta", "multiplicacion", "multiplicación", "division", "división"]:

        print("Operación no válida. Te invito a volver a intentarlo.")

        continue  # Vuelve al principio del bucle a pedir la operación otra vez
 
    # 2. Pedir el segundo número (con control de errores por si no es un número)

    try:

        num2 = float(input("Introduce el segundo número: "))

    except ValueError:

        print("Error: Debes introducir un número válido. Volvamos a empezar esta operación.")

        continue
 
    # 3. Realizar los cálculos

    if operacion in ["suma"]:

        resultado = num1 + num2

    elif operacion in ["resta"]:

        resultado = num1 - num2

    elif operacion in ["multiplicacion", "multiplicación"]:

        resultado = num1 * num2

    elif operacion in ["division", "división"]:

        if num2 == 0:

            print("Error: No se puede dividir entre cero.")

            continue

        resultado = num1 / num2
 
    # 4. Mostrar el resultado y realimentar la variable num1

    print(f"-> Resultado actual: {resultado}")

    print("-----------------------------------")

    num1 = resultado  # El resultado ahora es el primer número para la siguiente vuelta
 
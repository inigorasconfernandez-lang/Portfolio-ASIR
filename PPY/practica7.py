# Pedimos el número
while True:
    try:
        numero = int(input("Introduce un número entero: "))
        break
    except ValueError:
        print("Introduzca un valor numérico, por favor")

# El símbolo % nos da el resto de la división
if numero % 2 == 0:
    print("El número", numero, "es par")
else:
    print("El número", numero, "es impar")

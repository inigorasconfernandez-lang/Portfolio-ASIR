# Pedimos el número al usuario


while True:
    try:
        numero = int(input("Introduce un número:"))
        break
    except ValueError:
        print("Introduce un valor numerico, por favor")

# Comprobamos las condiciones
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

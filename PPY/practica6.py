# Pedimos los dos valores


while True:
    try:
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))
        break
    except ValueError:
        print("Introduce un valor numerico, por favor")

# Lógica de comparación


if a > b:
    print("De entre", a, "y", b, "el mayor es:", a)
else:
    if a < b:
        print("De entre", a, "y", b, "el mayor es:", b)
    else:
        print(a, "y", b, "son iguales")

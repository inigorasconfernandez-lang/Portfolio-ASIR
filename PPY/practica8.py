while True:
    try:
        n = float(input("Introduce el número n: "))
        m = float(input("Introduce el número m: "))
        break
    except ValueError:
        print("Escriba un valor númerico, por favor")

if m % m == 0:
    print("El", n, "es divisible entre", m)
else:
    print("El", n, "no es divisible entre", m)

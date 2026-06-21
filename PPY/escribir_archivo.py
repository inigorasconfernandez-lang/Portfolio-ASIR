'''Escribir en archivo'''

'''Escribir archivo'''
 
with open("append.txt", "a") as fichero:
    print("a")
    fichero.write("Hola este es un texto de prueba.\n")
    print("a")
    fichero.write("Esta es la segunda línea")

    with open("escribe.txt", "w") as fichero:
        print("b")
        fichero.write("La variable.\n")
        print("b")
        fichero.write("segunda.\n")
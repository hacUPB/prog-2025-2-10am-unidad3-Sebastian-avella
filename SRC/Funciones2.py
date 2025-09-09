"""
Crear una funcion llamada menu
parametros de entrada: ninguno
lo que realiza: muestra un menu y pide al usuario que seleccione
una opcion
valor de retorno: la opcion seleccionada
"""
def menu():
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("Elija una opcion"))
    return opcion

def entradas():
    print("1. Pan de bono\t\t%3000")
    print("2. Empanada\t\$3500")

def fuertes():
    print("sancocho \t\$20000")
    print("bamdeja paisa \t\%30000")

def bebidas():
    print("limonada de coco \t\$10000")
    print("jugos naturales \t\$7000")

def postres():
    print("pasteles \t\$5000")
    print("helados \t\$4000")

#Funcion principal
def main():
    eleccion = menu
    print(eleccion)

    match(eleccion):
        case 1:
            entradas()
        case 2:
            fuertes()
        case 3:
            bebidas()
        case 4:
            postres()
        case _:
            print("opcion no valida")
        
#Aqui se llama a la funcion main
if __name__ == "__main__":
    main()
while True:
    Combustible = int(input ("Ingrese la cantidad del combustible"))
    Altitud = int(input ("Ingrese la altitud "))
    Peso_aeronave = int(input ("Ingrese el peso_aeronave"))
    print("=== MENÚ PRINCIPAL ===")
    print("A. Combustible\nB. Altitud\nC Peso_aeronave\nD Salir")

    opcion = input("Selecciona una opción")
    opcion = opcion.upper()
    match opcion:
        case "A":
            print("Combustible")

        case "B":
            print("Altitud")

        case "C":
            print("Peso_aeronave")

        case "D":
            print("Salir")
        case _:
            print("Opción inválida.")




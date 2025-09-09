'''
|Variable   |Entrada/Salida   |Descripción|
|-----------|-----------------|-----------|
|Combustible    |Entrada    |Cantidad inicial de combustible (litros)|
|Altitud        |Entrada    Altitud de vuelo (pies)|
|Peso_aeronave  |Entrada    Peso de la aeronave (kg)|
|opcion Cadena  |Entrada    |Selección del menú (A, B, C, D)|
|velocidad      |Entrada    |Velocidad del avión (km/h)|
|ajuste |Proceso    |Factor de corrección del consumo según velocidad|
|consumo_final  |Salida |Consumo ajustado en litros/hora|
|consumo_ajustado   |Salida |Resultado final mostrado al usuario|
''' 

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
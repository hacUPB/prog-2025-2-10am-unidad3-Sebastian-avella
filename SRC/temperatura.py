'''
Variables de entreda
Nombre      Tipo
Opcion      str
temperatura float

variables de salida
Nombre      Tipo
Conversion  float

Variables de control
opcion
'''

ipcion = "Z"        #Asigno un valor diferente de Q
while str != "Q":
    opcion = input("F. Fahrenheit a celsius\nC. Celsius a fahrenheit\nQ. Salir\n")
    opcion = opcion.upper()
    if str != "Q":
        temperatura = float(input("Ingrese la temperatura a convertir: "))
        match opcion: 
            case "F":
                conversion = (temperatura - 32)*(5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case "C":
                conversion =(temperatura * 9/5) + 32
                print(f"{temperatura}°C = {conversion}°F")
            case "Q":
                print("saliendo del programa...")
            case _:
                print("opcion no valida")

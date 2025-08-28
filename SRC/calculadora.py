# calculadora
'''
control = True #variable booleana
while control == True:
    num1 = int(input ("Ingrese el primer numero"))
    num2 = int(input ("Ingrese el segundo numero"))
    print ("S. sumar\nR. Restar\nM. Multilicar\nD Dividir\nE. Salir")
    opcion = input("Elija una opcion")
    match opcion:
        case "S":
            print("Sumar")
            resultado = num1 + num2
        case "R":
            print("Restar")
            resultado = num1 - num2
        case "M":
            print("Multiplicar")
            resultado = num1 * num2
        case "D":
            print("Dividir")
            resultado = num1 / num2
        case "E":
            control = False
        case _:
            print ("Modo no válido")
    print (f"Resultado = {resultado}")
'''

#control = True #variable booleana
while True:
    num1 = int(input ("Ingrese el primer numero"))
    num2 = int(input ("Ingrese el segundo numero"))
    print ("S. sumar\nR. Restar\nM. Multilicar\nD Dividir\nE. Exponencial\nF. Salir")
    opcion = input("Elija una opcion")
    opcion = opcion.upper() #Se convierte el texto a mayúscula
    match opcion:
        case "S":
            print("Sumar")
            resultado = num1 + num2
        case "R":
            print("Restar")
            resultado = num1 - num2
        case "M":
            print("Multiplicar")
            resultado = num1 * num2
        case "D":
            print("Dividir")
            resultado = num1 / num2
        case "E":
            print("Exponencial")
            resultado = num1 ** num2
        case "F":
            break
        case _:
            print ("Modo no válido")
    print (f"Resultado = {resultado}")
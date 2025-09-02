# Tabla de multiplicar
numero = int(input("Ingrese número entero positivo: "))
while numero <= 0:
    print("Error: debe ser un número entero positivo.")
    numero = int(input("Ingrese número entero positivo: "))

print(f"Tabla de multiplicar de {numero}:")
i = 1
while i <= 15:
    print(f"{numero} x {i} = {numero * i}")
    i += 1




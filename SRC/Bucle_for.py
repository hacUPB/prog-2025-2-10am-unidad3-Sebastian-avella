'''
for cont in range(1, 20, 3):
    print(cont)
'''
# Escribe un programa que solicite al usuario ingresar un número entero positivo n. Luego, 
# utiliza un bucle for con la función range() para calcular la suma de todos los números pares desde 1 hasta n.
# Finalmente, muestra el resultado de la suma en pantalla.

# No se pueden ingresar valores negativos
#No puede pasar hasta que no ingrese un número positivo

n = int(input("Ingrese número entero positivo: "))
while n < 0:
    n = int(input("ingrese número entero positivo"))
acum = 0
for cont in range (1, n + 1):
    if cont % 2 == 0:
        acum += cont #acum = acum + cont
print(f"la suma de los pares:{acum}")


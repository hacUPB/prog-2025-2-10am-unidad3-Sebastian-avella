#determinar su número es par o impar
numero = int(input("Ingrese un numero entero: "))
residuo = numero % 2
#si residuo es 0, es par
if residuo == 0:
    print(numero, "es par")
#Si no es impar
else:
    print(numero, "es impar")

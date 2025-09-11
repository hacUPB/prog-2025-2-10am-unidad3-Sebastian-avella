'''
variable de entrada 
numero   int

variable de salida
divisores
'''

numero = int(input("ingrese un numero entero mayor que 1: "))
cont = 0
for i in range (1, numero + 1):
    if numero % i == 0:
        cont += 1 #cont = cont + 1

if cont == 2:
    print(f"{numero} es primo")
else:
    print (f"ls divisores de {numero} son:")
    for i in range (1, numero + 1):
        if numero % i == 0:
            print (i)
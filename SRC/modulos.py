'''
import mod_funciones
#funcion princial
numero = int(input("Ingrese un número mayor que 1: "))
mod_funciones.primo(numero)
variable = int(input("Ingrese el número de términos de la de serie de fibonnaci"))
mod_funciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
mod_funciones.tabla(multiplicando)
'''
from mod_funciones import *

def main():
    while True:
         opc = menu()
         match opc:
             case 1: 
                 print("Calcular si un número es primo")
                 valor = int(input("Ingrese un número entero mayor que 1"))
                 primo(valor)
             case 2:
                print("Imprime la serie de fibonacci")
                num = int(input("Ingrese el número de términos >> "))
                fibonacci(num)
             case 3:
                print("Imprime la tabla de multiplicar")
                num = int(input("ingrese el número >> "))
                tabla(num)
             case 4:
                 break
             case _:
                 print("La opcion que ingreso no es valida")
               

    

if __name__=="__main__":
    main()


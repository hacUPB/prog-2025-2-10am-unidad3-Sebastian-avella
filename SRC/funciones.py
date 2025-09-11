#Sección de las funciones
def suma(a,b):
    resultado = a + b
    return resultado    

def resta(num1,num2):
    res = num1 - num2
    return res

#Sección para el programa principal
#llamando a la funcion
numero1 = 5
numero2 = 3
#las vartiables pertenecen al contexto donde fueron creadas
a = 1000
b = 500
resultado_suma = suma(numero1,numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898, 564))
suma(45, 78)

res_resta = resta(a,b)
print(res_resta)

print(max(56,98))

texto = "La universidad Pontificia Bolivariana se encuentra en el barrio laureles de medellin"

x = texto.find ("laureles")

print(x)
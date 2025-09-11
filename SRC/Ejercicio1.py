print ("Ingresa tu nombre y apellido")
nombre = input ()
print ("Bienvenido: ")
#Opcion 2
print (nombre)
#Opcion 2
print ("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input("Ingresa tu peso en kilogramos: ")
peso = float(peso)
altura = input (" Ingresa tu talla en metros: ")
altura = float(altura)
imc = peso/altura**2
#Mostrar imc
print("Tu IMC = ", imc)

if imc >= 18.5 and imc <= 24.9:
    print("normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidad 1")
elif imc >= 35 and imc <= 39.9:
    print("obesidad 2")
elif imc >= 40:
    print("obesidad extrema 3")

    


if imc < 18.5:
    mensaje = "bajo peso"
elif imc < 25:
    mensaje = "peso normal"
elif imc < 35:
    mensaje = "obesidad tipo 1"
elif imc < 40:
    mensaje = "obesidad tipo 2"
else:
    mensaje = "obesidad extrema"

print(f"Paciente {nombre}, tiene un imc de {imc:0.2f} y su condicion es {mensaje}. ") 
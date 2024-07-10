import numpy as np
#Reto 1 - Multiplicar decimales
"""
Pide a tu usuario que ingrese 2 numeros con decimales (cuantos más mejor) y muestra el resultado de multiplicarlos __facil, no__

print ("Bienvenido al reto 1")

num_a = float(input("Ingresa un numero con decimales: "))
num_b = float(input("Ingresa otro numero con decimales: "))
resultado = num_a * num_b
print ("El resultado de la multiplicacion es: ", resultado)
"""

# Reto 2 - Reducir los decimales
"""
Toma como base el reto anterior, pero ajústalo para que el resultado muestre solamente 1, 2, 3 o 4 decimales.

print ("Bienvenido al reto 2")


num_a = float(input("Ingresa un numero con decimales: "))
num_b = float(input("Ingresa otro numero con decimales: "))
r_1= np.round(num_a * num_b,1)
r_2= np.round(num_a * num_b,2)
r_3= np.round(num_a * num_b,3)
r_4= np.round(num_a * num_b,4)
print ("El resultado de la multiplicacion es: ", r_1)
print ("El resultado de la multiplicacion es: ", r_2)
print ("El resultado de la multiplicacion es: ", r_3)
print ("El resultado de la multiplicacion es: ", r_4)
"""


#Reto 3 - Raíces cuadradas redondeadas
"""
Pide a tu usuario que ingrese un numero, cuyo valor debe ser mayor a 20, luego calcula su raiz cuadrada y reduce a 2 o 3 decimales el resultado final.

print("Bienvenido al reto 3")

num_a = float(input("Ingresa un numero mayor a 20: "))

def comparar (num_a):
  if num_a >= 20:
    a = np.sqrt(num_a)
    a= np.round(a,2)
    mensaje = f'La raiz cuadrada de {num_a} es: {a}'
  else:
    mensaje = "El numero ingresado es menor a 20"
  return mensaje
print(comparar(num_a))
"""

#Reto 4 - Calcular área de un círculo
"""
Solicita a tu usuario que ingrese un numero el cual será el radio de un circulo y con este dato calcula el area de un círculo.
Si tu lenguaje cuenta con librerias especificas para este propósito haz uso de las misma

print("Bienvenido al reto 4")

num_a = float(input("Ingresa un numero: "))

radio = np.sqrt(num_a / np.pi)

print(f'El area del circulo es: {num_a}, y su radio es: {np.round(radio,2)}')

"""


#Reto 5 - Calcular volumen de un cilindro
"""
Pide a tu usuario que indique el radio y la profundidad de un cilindro. Despues aplica la formula correspondiente para calcular el volumen del cilindro y reduce el resultado a un solo decimal.

print("Bienvenido al reto 5")

num_a=float(input("Ingresa el VOLUMEN del CILINDRO:  "))
num_b=float(input("Ingresa la ALTURA del CILINDRO:  "))

radio = np.sqrt(num_a/(np.pi*num_b))
radio = np.round(radio,1)

print(f'El VOLUMEN del CILINDRO es: {num_a}, la ALTURA es: {num_b}, y su radio es: {radio}')
"""

#Reto 6 - Mostrar enteros y residuos
"""
Pide al usuario que ingrese 2 numeros, dividelos, muestra un resultado como enteros y ademas el residuo por separado de una forma que seal facil de entender al usuario.
Por ejemplo: “9 dividido entre 2 es 4 y sobra 1”.

print("Bienvenido al reto 6")

num1 = int(input("Ingresa el primer número (dividendo): "))
num2 = int(input("Ingresa el segundo número (divisor): "))


cociente = num1 // num2
residuo = num1 % num2


print(f"{num1} dividido entre {num2} es {cociente} y sobra {residuo}.")
"""

#Reto 7 - Calcular perímetros y áreas
"""
Muestra un menu con distintas figuras geometricas, por lo menos 3 diferentes (triangulo, cuadrado, pentagono, etc.)
Tu usuario debe poder elegir alguna de estas figuras, indicar la distancia de sus lados y mostrar como resultado tanto el perímetro como el área de dicha figura.
"""

def calcular_perimetro_area_triangulo(lado):
  perimetro = lado * 3
  area = (np.sqrt(3) / 4) * lado ** 2
  return perimetro, area

def calcular_perimetro_area_cuadrado(lado):
  perimetro = lado * 4
  area = lado ** 2
  return perimetro, area

def calcular_perimetro_area_pentagono(lado):
  perimetro = lado * 5
  area = (1/4) * np.sqrt(5 * (5 + 2 * np.sqrt(5))) * lado ** 2
  return perimetro, area

def mostrar_menu():
  print("Bienvenido al Reto 7 - Calcular perímetros y áreas")
  print("Elige una figura geométrica:")
  print("1. Triángulo equilátero")
  print("2. Cuadrado")
  print("3. Pentágono regular")
  opcion = int(input("Ingresa el número de la opción: "))
  return opcion

def main():
  opcion = mostrar_menu()

  if opcion in [1, 2, 3]:
      lado = float(input("Ingresa la longitud del lado: "))

      if opcion == 1:
          perimetro, area = calcular_perimetro_area_triangulo(lado)
          figura = "triangulo equilatero"
      elif opcion == 2:
          perimetro, area = calcular_perimetro_area_cuadrado(lado)
          figura = "cuadrado"
      elif opcion == 3:
          perimetro, area = calcular_perimetro_area_pentagono(lado)
          figura = "pentagono regular"

      print(f"El perímetro del {figura} es: {perimetro}")
      print(f"El area del {figura} es: {area}")
  else:
      print("Opcion no valida. Por favor, elige una opcion del 1 al 3.")
    
if __name__ == "__main__":
  main()

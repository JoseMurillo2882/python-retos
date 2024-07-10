#Reto 1 - Curso favorito
"""
Pide a tu usuario que indique cual es su curso favorito de Platzi e imprimelo en pantalla 8 veces.

print("Bienvenido al reto 1")

curso=str(input("Ingresa tu curso favorito: ")).strip().lower()
print((f'Tu curso favorito es {curso}\n')*8)
"""


#Reto 2 - Curso favorito ‘n’ veces
"""
Toma el reto anterior, pero ahora pregunta al usuario cuantas veces quiere mostrar el mensaje.
¿Que pasa si coloca cero como respuesta? 🤔

print("Bienvenido al Reto 2")

curso = input("Ingresa tu curso favorito: ").strip().lower()
n = int(input("Ingresa la cantidad de veces: "))

if n >= 1:
    for i in range(n):
        mensaje = f'Tu curso favorito es {curso}, #{i + 1}'
        print(mensaje)
else:
    mensaje = f'El número {n} no es válido. Debes ingresar un número mayor o igual a cero.'
    print(mensaje)

"""


# Reto 3 - Curso en una columna
"""
Nuevamente, pide a tu usuario que indique su curso favorito de Platzi pero ahora muestra un caracter por linea de forma que puede parecer el inicio de un acrostico.

print("Bienvedio al Reto 3")

curso = str(input("Ingresa tu curso favorito: ")).strip().upper()

for letra in curso:
    print(letra)
"""

#Reto 4 - Animal en columna ‘n’ veces.
"""
Toma como base el reto anterior, pide a tu usuario que indique su animal favorito y después muestralo con un caracter por linea. Esto debe repetirse un numero de veces que ya hayas preguntado a tu usuario.

animal = input("Ingresa tu animal favorito: ").strip().upper()
n = int(input("Ingresa la cantidad de veces: "))

if n >= 1:
  for i in range(n):
     for letra in animal:
      print(letra)
"""

#Reto 5 - Tabla de multiplicar
"""
Pide a tu usuario un numero, luego de ello muestra la tabla de multiplicar de ese numero del 1 al 10.

print("Bienvenido al Reto 5")

numero=int(input("Ingresa un numero: "))

for i in range(1,11):
  print(f'{numero} x {i} = {numero*i}')
"""

#Reto 6 - Cuenta regresiva
"""
Pide a tu usuario un numero, despues imprime una cuenta regresiva uno a uno, desde ese numero hasta 0. Esto aplica tambien para numeros negativos.


print("Bienvenido al Reto 6")

numero=int(input("Ingresa tu numero: "))

if numero >= 0:
  for i in range(numero, -1, -1):
    print(i)
elif numero < 0:
  for i in range(numero, +1, +1):
    print(i)

"""
#Reto 7 - Curso favorito, sin exagerar
"""
Toma como base el Reto 2, pero agrega como condiciones las siguientes:

Si el número ‘n’ es mayor a 15, solo imprimirás el nombre del curso 3 veces e indicarás que ‘n’ es un número muy grande.


print("Bienvenido al Reto 7")

curso = input("Ingresa tu curso favorito: ").strip().lower()
n = int(input("Ingresa la cantidad de veces: "))

if n <= 0:
    mensaje = f'El número {n} no es válido. Debes ingresar un número mayor o igual a cero.'
    print(mensaje)
elif n < 15:
    for i in range(n):
        mensaje = f'Tu curso favorito es {curso}, #{i + 1}'
        print(mensaje)
else:
    
    for i in range(3):  
        mensaje = f'Tu curso favorito es {curso}, #{i + 1}'
        print(mensaje)
    print(f'El número {n} es un número muy grande.')
"""

# Reto 8 - Suma autorizada
"""
Crearas un programa que pedira a tu usuario 4 numeros, uno por uno. Al indicarlo preguntaras al usuario si desea sumarlo al total, si la respuesta es afirmativa se sumara. Al final debes mostrar el valor de la suma de aquellos numeros que fueron aceptados para la suma.

print("Bienvenido al Reto 8 - Suma autorizada")

suma = 0

for i in range(4):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    respuesta = input("¿Desea sumar este número al total? (si/no): ").strip().lower()

    if respuesta == "si":
        suma += numero

print(f"La suma de los números aceptados es: {suma}")
"""

#Reto 9 - Recta numérica
"""
Escribe un programa donde preguntes a tu usuario si desea una recta numerica positiva o negativa, despues pide un numero que servira como limite e imprime todos los numeros de uno en uno partiendo desde el cero.
"""  
print("Bienvenido al reto 9")

respuesta = str(input("Desea una recta numerica positiva o negativa:  ")).strip().lower()

limite=int(input("Cual es el limite de la recta  "))

if respuesta == "positiva" and limite >=1:
  for i in range(0,limite+1,1):
    print(i)
elif respuesta =="negativa" and limite <=-1:
  for i in range(0,limite-1,-1):
    print(i)

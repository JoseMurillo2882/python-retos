#Reto 1 - Suma hasta cincuenta
"""
Crea una variable que se llame total, despues pide a tu usuario que ingrese un numero y lo sume al valor de total. Haz que esto se repita hasta que el valor de total sea mayor a 50 y muestra el resultado en pantalla.

print("Bienvenido al Reto 1")
total = 0

while total < 50:
  num=float(input("Ingresa un numero: "))
 
  total = num + total
  print("El total es: ", total)
"""

#Reto 2 - Más allá del cuarenta y dos
"""
Crea un codigo que pida al usuario un numero y se repita hasta que coloque un numero mayor a 42. Cuando se cumpla esta condicion muestra el resultado en pantalla indicando esto al usuario y finaliza el ciclo.

print("Bienvedio al reto 2")

num = 0
while num < 42:
  num = float(input("Ingresa un numero: "))
  print("El numero ingresado es: ", num)
  
print("El numero ingresado es mayor a 42")
"""

#Reto 3 - Sumas consecutivas
"""
Pide al usuario que ingrese dos numeros y los sume. Despues pregunta siquiere añadir otro número: si la respuesta es afirmativa añadelo al total; en caso contrario finaliza el ciclo y muestra el resultado total en pantalla.

print("Bienvenido al reto 3")


num1=float(input("Ingresa el PRIMER numero: "))
num2=float(input("Ingresa el SEGUNDO numero: "))
r=str(input("¿Quieres añadir otro numero? ")).strip().lower()
total = num1 + num2

while r == "si":
  num3=int(input("¿Ingresa el nuevo numero? "))
  total = total + num3
  r=str(input("¿Quieres añadir otro numero? ")).strip().lower()

  
print(f"El resultado total es: {total}")
"""

#Reto 4 - Lista de invitados
"""
Estas organizando un banquete al que quieres invitar a tus amigos. Crea un programa que pida el nombre de uno de tus amigos, al hacerlo aumenta en uno una variable contadora, después pregunta si quieres invitar a alguien mas: si la respuesta es afirmativa entonces pregunta por una persona mas; en caso contrario cierra el ciclo y muestra en pantalla cuantos invitados son.

print("Bienvenido al reto 4")

contador = 0
while True:
  nombre = input("Ingresa el nombre de un amigo: ")
  contador += 1
  print("El numero de invitados es: ", contador)
  r = input("¿Quieres invitar a alguien mas? ").strip().lower()
  if r != "si":
    break

print(f"El numero de invitados es: {contador}")
"""
#Reto 5 - Adivina el número secreto
"""
Crea un programa donde tendras la variable numero_secreto, la cual toma un valor aleatorio entre 1 y 100. DespuEs pide a tu usuario que indique un numero para intentar adivinarlo: en caso de acertar indicale cual era el numero secreto y cuantos intentos le tomo; en caso contrario indicale si el número ingresado es mayor o menor al numero secreto.


print("Bienvenido al reto 5")

import random
numero_secreto = random.randint(1, 100)
intentos = 0
numero = 0

while numero != numero_secreto:
    intentos += 1
    numero = int(input("Ingresa un numero: "))

    if numero < numero_secreto:
        print("El numero secreto es mayor al numero ingresado.")
    elif numero > numero_secreto:
        print("El numero secreto es menor al numero ingresado.")
    else:
        print(f"¡Felicidades! El numero secreto es: {numero_secreto}. Lo encontraste en {intentos} intentos.")
"""


#Reto 6 - “Un elefante se balanceaba…”
"""
Escribe un programa que inicie mostrando en pantalla la letra de “Un elefante se balanceaba” iniciando con el número 1, después pregunta al usuario cuantos elefantes más se balancearán y debe responder un número más al mostrado. En caso de ingresar un número diferente pedirle que intente de nuevo y repetir el ciclo hasta tener 10 elefantes.
Tomar en cuenta cuando el texto muestra un solo elefante y varios elefantes.
"""
print("Bienvenido al reto 6")

elefantes = 1
print(f"{elefantes} elefante se balanceaba sobre la tela de una araña")

while elefantes < 10:
    respuesta_correcta = elefantes + 1
    a = int(input(f"¿Cuántos elefantes se balancearán ahora? (Debe ser {respuesta_correcta}): "))

    if a == respuesta_correcta:
        elefantes += 1
        if elefantes == 1:
            print(f"{elefantes} elefante se balanceaba sobre la tela de una araña")
        else:
            print(f"{elefantes} elefantes se balanceaban sobre la tela de una araña")
    else:
        print(f"Intenta de nuevo. Debes ingresar {respuesta_correcta}.")

print("Ahora hay 10 elefantes balanceándose sobre la tela de una araña")

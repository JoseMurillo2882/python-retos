# Reto 1 Longitud del string
""""
Pide a tu usuario que ingrese el nombre de su curso favorito, 
obten la longitud de ese string y muestralo en pantalla.


print ("Bienvenido al reto 1")

word_a=str(input("Ingresa el nombre de tu curso: ")).strip().lower()

longitud=len(word_a)

print(f'La longitud de la palabras: {word_a} es de: {longitud}')
"""



#Reto 2 __Suma__ de strings
"""
Crea un programa en el que le pidas en 3 variables distintas:
nombre, apellido y comida favorita. Como salida mostraras el 
mensaje Hola, mi nombres es {nombre} {apellido} y mi comida 
favorita es {comida} en un solo string.

print("Bienvenido al reto 2")

a=str(input("Ingresa tu NOMBRE: ")).strip()
b=str(input("Ingresa tu APELLIDO: ")).strip()
c=str(input("Ingresa tu COMIDA: ")).strip()

print(f"Hola, mi nombre es {a} {b} y mi comida favorita es {c}")
"""


#Reto 3 Ajusta las iniciales
"""
Ahora, pediras a tu usuario que ingrese su nombre, apellido y país de origen en minusculas. 
Despues mostraras los datos de salida con mayuscula inicial al tratarse de nombres propios.

print("Bienvenido al reto 3")

a=str(input("Ingresa tu NOMBRE:  ")).strip().lower()
b=str(input("Ingresa tu APELLIDO:  ")).strip().lower()
c=str(input("Pais de ORIGEN:  ")).strip().lower()

print(f"Tu nombre es: {a.capitalize()} {b.capitalize()}, tu pais de origen es: {c.capitalize()}")
"""



#Reto 4 String fragmentado
"""
Pongamonos mas exigentes 💥
Solicita a tu usuario que indique una oracion de 10 o mas caracteres, la línea de un poema o cancion funcioona excelente.
Calcula la longitud del string, pide un numero de rango inicial y final que este entre la longitud del string para al final
mostrar el fragmento que incluya los caracteres en ese intervalo.

print("Bienvenido al reto 4")

a=str(input("Ingresa una oracion de minimo de 10 caracteres:  ")).strip().lower()

while len(a) < 10:

    a=str(input("Ingresa una oracion de minimo de 10 caracteres:  ")).strip().lower()

longitud=len(a)
print(f"La longitud de tu oracion es de: {a}")

rango_inicial = int(input(f"Ingresa un numero de rango inicial (0 a {longitud-1}): "))
rango_final = int(input(f"Ingresa un numero de rango final ({rango_inicial} a {longitud}): "))

while rango_inicial < 0 or rango_final > longitud or rango_inicial >= rango_final:
    print("Los rangos ingresados no son validos. Intentalo de nuevo.")
    rango_inicial = int(input(f"Ingresa un numero de rango inicial (0 a {longitud-1}): "))
    rango_final = int(input(f"Ingresa un numero de rango final ({rango_inicial} a {longitud}): "))

# Mostrar el fragmento del string en el intervalo especificado
fragmento = a[rango_inicial:rango_final]
print(f"El fragmento de la oracion en el intervalo {rango_inicial}-{rango_final} es: '{fragmento}'")

"""


#Reto 5 Mayusculas y minusculas
"""
Solicita a tu usuario que indique 2 palabras, donde al mostrarlas en pantalla una estara 
totalmente en mayusculas y otra en minusculas __facil, no__

print("Bienvenido al reto 5")

a=str(input("Ingresa la PRIMERA palabra:  ")).strip().lower()
b=str(input("Ingresa la SEGUNDA palabra:  ")).strip().upper()

print(f"La PRIMERA palabras es: {a}, la SEGUNDA palabras: {b}")
"""

#Reto 6 Nombres cortos y largos
"""
Ya sabemos trabajar con nombres __pero que pasa si cumple ciertas cualidades__
Tu usuario ingresara su nombre, si tiene una longitud mayor a 5 caracteres mostraras
un saludo con su nombre en pantalla. Si tiene menos de 5 caracteres, pediras su apellido,
mostraras el saludo con nombre y apellido. En ambos casos deberas mostrarlos con mayuscula inicial.


print("Bienvenido al reto 5")

nombre=str(input("Ingresa tu NOMBRE:  ")).strip().lower()
nombre_1=len(nombre)

def respuesta (nombre):
    
    if nombre_1 >= 5:
        mensaje = f"Te saudo a ti {nombre.capitalize()}"
        print(mensaje)
    
    elif 5 > nombre_1:
        apellido=str(input("Ingresa tu APELLIDO:  ")).strip().lower()

        mensaje = f"Te saudo a ti {nombre.capitalize()} {apellido.capitalize()}"
        print(mensaje)

respuesta(nombre)

"""

#Reto 7 ¡Hablemos Pig Latin! (Puerco Latino) 
"""
Solo una cosa, pide a tu usuario que ingrese una palabra y traddcela a Pig Latin.

Espera ¡que!
PuercoLatino es como el idioma de la __efe__, donde cambiamos las palabras bajo ciertas condiciones. En este caso sera así:

La primer consonante de una palabra se pasa al final y se agrega la sílaba __ay__.
Si una palabra inicia con vocal, se agrega __way__ al final.
Ejemplos:

Platzi =====> Latzipay
Abeja ======> Abejaway
"""

print("Bienvenido al reto 7 - Hablemos Pig Latin!")


def traducir_a_pig_latin(palabra):
    vocales = "aeiouAEIOU"
    if palabra[0] in vocales:
        return palabra + "way"
    else:
        return palabra[1:] + palabra[0] + "ay"


palabra = input("Ingresa una palabra: ").strip()


traduccion = traducir_a_pig_latin(palabra)


print(f"La palabra '{palabra}' en Pig Latin es: '{traduccion}'")




 
    
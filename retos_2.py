# Reto 1 - Numero mayor y menor
"""
Escribe un programa que pida al usuario 2 numeros, mostrando como salida 
cual es el numero mayor y la diferencia de uno respecto al otro. 
En caso de que los numeros sean iguales, mostrarlo tambien en pantalla.

print("Bienvenido al reto 1")

num_a = float(input("Ingresa un numero A: "))
num_b = float(input("Ingresa un numero B: "))

def comparacion(num_a, num_b):
    if num_a > num_b:
        diferencia = num_a - num_b
        mensaje = f'El numero A: {num_a}, es MAYOR que el numero B: {num_b}. La diferencia es {diferencia}.'
        print(mensaje)
    elif num_b > num_a:
        diferencia = num_b - num_a
        mensaje = f'El numero B: {num_b}, es MAYOR que el numero A: {num_a}. La diferencia es {diferencia}.'
        print(mensaje)
    else:
        mensaje = f'El numero A: {num_a}, es IGUAL que el numero B: {num_b}.'
        print(mensaje)

comparacion(num_a, num_b)
"""

#Reto 2 - En el rango, por favor.
""""
Pide al usuario que indique 2 numeros: uno que servira como limite y otro 
para comparar. Si el segundo numero es menor al primero, mostraras un mensaje 
diciendo El numero x se encuentra en el rango, gracias y en caso contrario 
dira - El numero x excede el limite permitido. -

print("Bienvenido al reto 2")

num_a=int(input("Ingresa tu numero A: "))
num_b=int(input("Ingresa tu numero B: "))

def comparar (num_a,num_b):
    if num_b < num_a:
        mensaje = f'El numero B:{num_b} se encuentra en el rango, gracias'
        print(mensaje)
    else:
        mensaje = f'El numero B: {num_b} excede el limite permitido.'
        print(mensaje)
        
comparar(num_a, num_b)
"""

#Reto 4  -I like turtles
"""
Escribe un programa que pida al usuario ingrese su animal favorito, 
si coloca __Tortuga__, __tortuga__, __TORTUGA__ o cualquier otra variante 
de la palabra entonces mostrar en pantalla __Tambien me gustan las tortugas__.
En caso contrario mostrar el mensaje __Ese animal es genial, pero prefiero las tortugas__.

print("Bienvenido al Reto 4")

animal_a = str(input("Ingresa tu animal favorito: ")).strip().lower()
tortuga = "tortuga"

def comparar (animal_a,tortuga):
    if(animal_a == tortuga):
        mensaje=f'Tambien me gustan las tortugas'
        print(mensaje)
    else:
        mensaje=f'Ese animal: {animal_a}, es genial, pero prefiero las tortugas'
        print(mensaje)

comparar(animal_a,tortuga)
"""


#Reto 5 - __Como esta el clima__
"""
Crea un programa que pregunte al usuario si esta lloviendo, 
en caso de responder __SI__ pregunta si esta haciendo mucho viento
y si responde __SI__ nuevamente muestra un mensaje indicando que hace
mucho viento para salir con una sombrilla. En caso contrario, anima 
al usuario a que lleve una sombrilla. Para el caso de responder __NO__
en la primer pregunta, entonces solo desea un bonito dia.
Considera que las respuestas pueden pasarse a minusculas para evitar posibles errores.

print("Bienvenido al RETO 5")

clima = str(input("El dia de hoy esta __LLUVIENDO__:")).strip().lower()


def decision (clima):
    if clima == "si":
        estado= str(input("El dia de hoy esta __VIENTO__:")).strip().lower()
        if estado == "si":
            mensaje=f'Hace mucho viento para salir con una sombrilla'
            print(mensaje)
        else:
            mensaje=f'Lleva una sombrilla '
            print(mensaje)
    else:
        mensaje_1 = "Ten un bonito dia"
        print(mensaje_1)

decision(clima)
"""

#Reto 6 - Edad permitida
"""
Pide al usuario que ingrese su edad y mostraras un mensaje correspondiente si esta coincide con las siguientes condiciones:
Mas de 30 anos: Nunca es tarde para aprender __Que curso tomaremos__
Entre 29 y 18 anos: Es un momento excelente para impulsar tu carrera.
Menos de 18 anos: __Sabes hacia donde dirigir tu futuro__ Seguro puedo ayudarte.


print("Bienvenido al Reto 6")

edad = int(input("Ingresa tu EDAD: "))

def comparar (edad):
    if edad >=30:
        mensaje = f'Tu edad es de {edad} y nunca es tarde para aprender'
    elif 18 <= edad <= 29:
        mensaje= f'Tu edad es de {edad} y es un momento excelente para impulsar tu carrera.'
    else:
        mensaje= f'Tu edad es de {edad} y sabes hacia donde dirigir tu futuro.'
    print(mensaje)
    
comparar(edad)

"""

#Reto 7 - Mensajes opcionale

"""
Crearas un un script para el que el usuario indicara un numero entre 1 y 6. Como respuesta se le brindara un mensaje segun el numero leido:
1 - Hoy aprenderemos sobre prorgamacion
2 - Que tal tomar un curso de marketing digital
3 - Hoy es un gran día para comenzar a aprender de diseno
4 - Y si aprendemos algo de negocios online
5 - Veamos un par de clases sobre produccion audiovisual
6 - Tal vez sea bueno desarrollar una habilidad blanda en Platzi
En caso indicar un numero distinto, pedir al usuario que ingrese uno en el rango valido.
"""

print("Bienvenido al reto 7")


def comparar (num_a):
    sw ={ 
        1 : 'Hoy aprenderemos sobre prorgamacion',
        2 : "Que tal tomar un curso de marketing digital",
        3 : "Hoy es un gran día para comenzar a aprender de diseno",
        4 : "Y si aprendemos algo de negocios online",
        5 : "Veamos un par de clases sobre produccion audiovisual",
        6 : " Tal vez sea bueno desarrollar una habilidad blanda en Platzi"
        }
    
    return sw.get(num_a, "Opcion Invalida ")

num_a=int(input("Ingrese el numero para seleccionar la Lista:"))

print(comparar(num_a))




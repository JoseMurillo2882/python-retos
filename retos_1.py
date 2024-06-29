#RETO 01
#print ("BIENVENIDO AL RETO 1")
#nombre = str(input("Introduce tu nombre: " ))

#print(f'Hola {nombre},un gusto saludarte')

#RETO2
#print ("BIENVENIDO AL RETO 2")
#nombre = str(input("Introduce tu nombre: " ))
#apellido = str(input("Introduce tu apellido: " ))

#print(f'Hola {nombre} {apellido},un gusto saludarte')	

#RETO3
#print ('BIENVENIDO AL RETO 3')
#curso_a = str(input("Introduce el nombre del curso: "))
#curso_b = str(input("Introduce el nombre del curso: "))
#curso_c = str(input("Introduce el nombre del curso: "))
#curso_d = str(input("Introduce el nombre del curso: "))
#cursos = [curso_a, curso_b, curso_c, curso_d]

#print("Plazti cuenta con los siguientes cursos: " )
#for curso in cursos:
  #print(curso)

#RETO4
"""
print("BIENVENIDO AL RETO 4")

numero_a = float(input("Ingresa tu numero: "))
numero_b = float(input("Ingresa tu numero: "))

decimales_a = str(numero_a).split('.')[1]
decimales_b = str(numero_b).split('.')[1]

print("Numeros decimales A",decimales_a)
print("Numeros decimales B",decimales_b)
print('El Resultado de tu suma es: ',numero_a + numero_b)

"""
"""
#RETO5
print("Bienvenido al reto 5")

numero_a = float(input("Ingresa numero A: "))
numero_b = float(input("Ingresa numero B: "))
numero_c = float(input("Ingresa numero C: "))

d = numero_a + numero_b
e = d * numero_c

decimal_a =str(numero_a).split('.')[1]
decimal_b =str(numero_b).split('.')[1]
decimal_c =str(numero_c).split('.')[1]


print("Decimal A: ",decimal_a)
print("Decimal B: ",decimal_b)
print("Decimal C: ",decimal_c)
print("El resultado de la operacion es: ",e)

"""
"""
#RETO 06
print("Bienvenido al RETO 6")

num_a= int(input("Ingresa cantidad de pizzas: "))
num_b= int(input("De cuantas rebanadas es la pizza: "))
num_c= int(input("Ingresa cantidad de personas: "))
num_d= int(input("Ingresa cantidad de rebanadas por persona: "))


d = (num_a * num_b) - (num_c * num_d)

print("Rebanadas Restantes: ",d)

"""
"""
#RETO 07

print("Bienvenido al RETO 7")

def age ():
  a=str(input("Ingresa tu nombre: "))
  b=int(input("Ingresa tu edad actual: "))
  c=b+1
  d=b-1

  mensaje= f'Hola, {a} el ano pasado tenias {d} y el proximo ano cumpliras {c}'

  print(mensaje)

age()
"""
"""
#RETO 08

print("Bienvenido al RETO 8")

a=int(input("Cuanto es la cuenta a pagar: "))
b=int(input("Cuantas personas son: "))
c=int(input("Porcentaje de propina: "))
d=int(input("De cuanto son los impuestos: "))

def cuenta(a,b,c,d):
  #porcentaje de propina
  porcentaje_a= (a*c)/100
  #porcentaje de impuestos
  porcentaje_b= (a*d)/100

  #total a pagar
  total = a + porcentaje_a + porcentaje_b

  total_a = total / b 

  print("El total a pagar con propina e impuestos es: ",total)
  print("La cantidad para cada persona es: ",total_a)

cuenta(a,b,c,d)
  
"""
"""
#RETO 09
print("Bienvenido al reto 9")

a=int(input("Ingrese la cantidad de dias: "))

def conversion(a):
  horas = a*24
  minutos = horas*60
  segundos = minutos*60

  print(f'La cantidad de dias {a} equivale a: {horas} horas, {minutos} minutos y {segundos} segundos')

conversion(a)
"""

"""
#RETO 10

print("Bienvenido al reto 10")

a= float(input("Ingrese la cantidad de MILLAS: "))

def distancia(a):
  km = a*1.609344

  print(f'La cantidad de {a} millas equivale a: {km} kilometros')

distancia(a)
"""

#RETO 11

print("Bienvenido al reto 11")

a= float(input("Ingres un numero mayor a '1000': "))
b= float(input("Ingresa un numero menor a '100': "))

if a>=1000 and b<=100:
      def cant_veces (a,b):
        num_veces = a/b
        print(f'El numero {b} cabe {num_veces} veces en el numero {a}')
       
else:
    a = float(input("Escribi un numero mayor a 1000"))
    b = float(input("Escribi un numero menor a 100"))
    

cant_veces(a,b)


 

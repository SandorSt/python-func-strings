import math
# 1. Escribir una función que reciba dos números y devuelva su producto.
# 2. Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py) que
# pida al usuario dos números, y luego muestre el producto.

def producto():

    num1 = int(input("Escribe un numero: "))
    num2 = int(input("Escribe un segundo numero: "))
    prod = num1 * num2
    print("El producto es : ", prod)

#producto()

# 3. Escribir funciones que permitan:
# a) Calcular el perímetro de un rectángulo dada su base y su altura.

def peri_rect(base, altura):
    peri = 2 * base + 2 * altura
    print(peri)

#peri_rect(2, 4)

# b) Calcular el área de un rectángulo dada su base y su altura.

def area_rect(base, altura):
    area = base * altura
    print(area)

# c) Calcular el perímetro de un círculo dado su radio.

def peri_circ(radio):
    peri = 2 * math.pi * radio
    print(peri)


# e) Calcular el área de un círculo dado su radio.

def area_circ(radio):
    area = math.pi * radio ** 2
    print(area)

# f) Calcular el volumen de una esfera dado su radio.

def vol_esf(radio):
    vol = 4 / 3 * math.pi * radio ** 3
    print(vol)

# g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

def hipotenusa(cat1, cat2):
    hipo = math.sqrt(cat1 ** 2 + cat2 ** 2)
    print(hipo)

#4. Analizar los siguientes bloques de código. ¿Cuál será el resultado de ejecutarlos?
#Verificar la respuesta con el intérprete.
#a) 
for i in range(5):
 print(i * i)

#b) 
for i in range(2, 6):
 print(i, 2 ** i)

#5. Escribir una función que, dado un número entero n, permita calcular su factorial.

def factorial(n):
    fact  = 1
    for i in range(1,n+1):
        fact = i * fact
    print(fact)

# 6. Escribir funciones que resuelvan los siguientes problemas:
# a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.

def mat(num1, num2):
    print("Suma :", num1 + num2, "\nResta:", num1 - num2, " \nDivision:", num1 / num2, "\nMultipliacion:", num1 * num2)

# b) Dado un número entero n, imprimir su tabla de multiplicar.

def tabla_mult(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

# 7. Escribir un programa que le pida una palabra al usuario, para luego imprimirla
# 1000 veces, en una única línea, con espacios intermedios.
# Ayuda: Investigar acerca del parámetro end de la función print.

def print_word():
    print(input("Escribe una palabra para imprimir: ")* 1000, end = " ")

# 8. a) Escribir una función que dado un número entero devuelva 1 si el mismo
# es impar y 0 si fuera par.

def par_impar(num):
    if num % 2 == 0:
        print(0)
    else:
        print(1)

# b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar
# y 1 si fuera par.

def impar_par(num):
    if num % 2 == 0:
        print(1)
    else:
        print(0)

# c) Escribir una función que dado un número entero devuelva el dígito de las
# unidades. Por ejemplo, para 153 debe devolver 3.

# d) Escribir una función que dado un número devuelva el primer número múltiplo de
# 10 inferior a él. Por ejemplo, para 153 debe devolver 150.
# 9. Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.
# 10. Escribir un programa que le pregunte al usuario un número n e imprima los
# primeros n números triangulares, junto con su índice. Los números triangulares se obtienen
# mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los
# primeros 5 números triangulares, el programa debe imprimir:
# 1 - 1
# 2 - 3
# 3 - 6
# 4 - 10
# 5 - 15
# 11. Escribir un programa que tome una cantidad m de valores ingresados por el
# usuario, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio
# de factorial e imprima el resultado junto con el número de orden correspondiente.
# 12. Escribir un programa que imprima por pantalla todas las fichas de dominó, de
# una por línea y sin repetir.
# 13. Modificar el programa anterior para que pueda generar fichas de un juego que
# puede tener números de 0 a n.
# 14. Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos.
# 15. Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario
# dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y
# muestre por pantalla la duración total en horas, minutos y segundos.
# 16. Escribir una función que reciba por parámetro una dimensión n, e imprima la
# matriz identidad correspondiente a esa dimensión.
# 17. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por
# 100, excepto que también sea divisible por 400.
# b) Dado un mes y un año, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa
# fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo
# transcurrido
# entre ambas, en años, meses y días.
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
# 18. Suponiendo que el primer día del año fue lunes, escribir una función que reciba un
# número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca.
# Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver
# 'martes'.
# 19. Escribir un programa que reciba como entrada un entero representando un
# año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en
# números romanos.
# 20. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
# y el programa le debe decir a qué signo corresponde.
# Acuario: 21 de enero al 20 de febrero.
# Piscis: 21 de febrero al 20 de marzo.
# Aries: 21 de marzo al 20 de abril.
# Tauro: 21 de abril al 20 de mayo.
# Geminis: 21 de mayo al 20 de junio.
# Cancer: 21 de junio al 20 de julio.
# Leo: 21 de julio al 20 de agosto.
# Virgo: 21 de agosto al 20 de septiembre.
# Libra: 21 de septiembre al 20 de octubre.
# Escorpio: 21 de octubre al 20 de noviembre.
# Sagitario: 21 de noviembre al 20 de diciembre.
# Capricornio: 21 de diciembre al 20 de enero.
# 21. Escribir un programa que permita al usuario ingresar un conjunto de notas,
# preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio
# correspondiente.
# 22. Escribir una función que reciba un número entero k e imprima su descomposición en
# factores primos.
# 23. Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al
# usuario la contraseña, y no le permita continuar hasta que la haya ingresado
# correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de
# intentos.
# c) Modificar el programa anterior para que después de cada intento agregue una
# pausa cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el
# usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True
# o False).
# 24. Números perfectos y números amigos
# a) Escribir una función que devuelva la suma de todos los divisores de un número n,
# sin
# incluirlo.
# b) Usando la función anterior, escribir una función que imprima los primeros m
# números
# tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m
# números
# perfectos).
# c) Usando la primera función, escribir una función que imprima las primeras m
# parejas
# de números (a, b), tales que la suma de los divisores de a es igual a b y la suma de
# los
# divisores de b es igual a a (es decir las primeras m parejas de números amigos).
# d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de
# ejecución.
# 25. Escribir un programa que le pida al usuario que ingrese una sucesión de números
# naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como
# condición de salida). Al final, el programa debe imprimir cuántos números fueron
# ingresados, la suma total de los valores y el promedio.
# 26. Escribir una función que reciba dos números como parámetros, y devuelva cuántos
# múltiplos del primero hay, que sean menores que el segundo.
# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta
# que
# sea mayor que el segundo.
# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos
# operaciones?
# 27. Escribir una función que reciba un número natural e imprima todos los números primos
# que hay hasta ese número.
# 28. Escribir una función que reciba un dígito y un número natural, y decida numéricamente
# si el dígito se encuentra en la notación decimal del segundo.
# 29. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje
# necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un
# grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios
# resueltos por el alumno, indicando con un valor centinela que no hay más examenes a
# revisar. Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios
# resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si
# aprobó o no.
# Cadenas de caracteres
# 30 Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres.
# b) Imprima los tres últimos caracteres.
# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
# 'reflejoojelfer'.
# 31. Escribir funciones que dada una cadena y un caracter:
# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
# 's,e,p,a,r,a,r'
# b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
# debería devolver 'mi_archivo_de_texto.txt'
# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
# 'X' debería devolver 'su clave es: XXXX'
# d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
# '255.255.255.0'
# 32. Modificar las funciones anteriores, para que reciban un parámetro que indique la
# cantidad máxima de reemplazos o inserciones a realizar.
# 33 Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si
# recibe
# '1234567890', debe devolver '1.234.567.890'.
# 34.. Escribir una función que dada una cadena de caracteres, devuelva:
# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
# devolver 'USB'.
# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
# 'república argentina' debe devolver 'República Argentina'.
# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
# debe devolver 'Antes ayer'
# 35. Escribir funciones que dada una cadena de caracteres:
# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
# 'logaritmos' debe devolver 'lgrtms'.
# b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
# devolver 'i ooae'.
# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
# devolver 'vistaerou'.
# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# 36. Escribir funciones que dadas dos cadenas de caracteres:
# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
# es una subcadena de 'subcadena'.
# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
# debe devolver 'gnome'.
# Ejercicio 6.8. Escribir una función que reciba una cadena de unos y ceros (es decir, un
# número
# en representación binaria) y devuelva el valor decimal correspondiente.
# Ejercicio 6.9. Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
# el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
# número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario
# y
# pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo
# debe
# devolver.
# Ejemplo:
# >>> z = pedir_entero("¿Cuál es tu número favorito?", -50, 50)
# ¿Cuál es tu número favorito? [-50..50]:
# 10
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: hola
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: -60
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: 51
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: -16
# >>> z
# -16
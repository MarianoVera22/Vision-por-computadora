# A. Crear una función adivina que permita adivinar un número secreto generado en
# 	forma aleatoria, según las siguientes consignas:
# 	El número secreto debe estar entre 0 y 100, y debe ser generado dentro de la función.
# 	La función adivina debe recibir un parámetro que indique la cantidad de intentos permitidos.

# B. Luego escribir un programa adivinador.py que:
# 	pida al usuario que adivine el número secreto, es decir que ingrese un número
# 	entre 0 y 100,
# 	use la función adivina anterior para verificar si adivinó (todo en el mismo archivo),
# 	si el usuario adivinó el número secreto antes de superar la cantidad permitida de
# 	intentos, imprima un mensaje con el número de intentos en los que adivinó.
# 	En caso de que esta cantidad de intentos sea superada el programa debe terminar
# 	con un mensaje.

# C. Finalmente ejecutar el programa adivinador.py desde la consola.

# Ayuda: código para generar un número aleatorio
# import random
# ...
# numero = random.randint(0, 100)
# ...

import adivina
import random

candidato=int(input('Ingresar numero entero entre 0 y 100: ')) # Entrada por teclado
adivina.adivinando(candidato) # Llamada a la funcion adivinando del archivo .py adivina


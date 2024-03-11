# A. Crear una función adivina que permita adivinar un número secreto generado en
# 	forma aleatoria, según las siguientes consignas:
# 	- El número secreto debe estar entre 0 y 100, y debe ser generado dentro de la función.
# 	- La función adivina debe recibir un parámetro que indique la cantidad de intentos permitidos.

# B. Luego escribir un programa adivinador.py que:
# 	- Pida al usuario que adivine el número secreto, es decir que ingrese un número
# 	entre 0 y 100,
# 	- use la función adivina anterior para verificar si adivinó (todo en el mismo archivo),
# 	- si el usuario adivinó el número secreto antes de superar la cantidad permitida de
# 	intentos, imprima un mensaje con el número de intentos en los que adivinó.
# 	- En caso de que esta cantidad de intentos sea superada el programa debe terminar
# 	con un mensaje.

# C. Finalmente ejecutar el programa adivinador.py desde la consola.

# Ayuda: código para generar un número aleatorio
# import random
# ...
# numero = random.randint(0, 100)
# ...

import random
numero = random.randint(0, 100)


def adivinando(candidato):
    contador = 0
    jugando = True

    while jugando:
        contador = contador+1
        if contador < 10:
            if candidato == numero:
                print('Felicidades adivinaste en {} intentos!'.format(contador))
                jugando = False
            elif candidato < numero:
                print('Mas alto')
                candidato = int(
                    input('Ingresar numero entero entre 0 y 100: '))
            else:
                print('Mas bajo')
                candidato = int(
                    input('Ingresar numero entero entre 0 y 100: '))
        else:
            print('Superaste el numero de intentos')
            jugando = False
    else:
        print('\nEl bucle de while termino')

    print('\nHecho')

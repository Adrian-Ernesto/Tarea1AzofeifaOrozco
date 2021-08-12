# TAREA 1 - MT7003
# ADRIAN OROZCO RIVERA-KARINA AZOFEIFA AMPIE


# USO DE PYTEST PARA PRUEBA DE FUNCIONES
# SE IMPORTAN LAS LIBRERIAS USADAS PARA GENERAR ARGUMENTOS ALEATORIOS
import math
import random
import string
# SE IMPORTAN LAS FUNCIONES DEL ARCHIVO CORRESPONDIENTE
from Funciones import multiple_op
from Funciones import verify_array_op
# PARAMETROS PARA LLAMAR A LAS FUNCIONES CON NUMEROS Y LETRAS ALEATORIOS
# NUMERO SE USA PARA INTRODUCIR STRING EN POSICION ALEATORIA PARA CASO DE ERROR
numero = random.randint(0, 2)
contador = 0  # VARIABLE DE CONTROL DE CICLOS WHILE
# NUMEROS ALEATORIOS USADOS COMO ARGUMENTOS Y ELEMENTOS DE LISTA
x = random.randint(1, 10)
y = random.randint(1, 10)
flag = 0  # VARIABLE DE CONTROL PARA ASEGURAR QUE LA LISTA SERA DE 3 ELEMENTOS
A_A = []  # LA VARIABLE A_A SIGNIFICA ARREGLO_ALEATORIO
Arreglo_aleatorio1 = []  # LISTA USADA EN CASO DE ERROR DE VERIFY_MULTIPLE_OP
# LOS SIGUIENTES CICLOS WHILE SE USAN PARA GENERAR LOS ARREGLOS
while contador < 3:
    A_A.append(random.randint(1, 10))
    contador = contador + 1
contador = 0
while contador < 3:
    if(contador == numero):
        # SE INSERTA UN STRING EN UNA POSICION ALEATORIA EN LA LISTA
        Arreglo_aleatorio1.append(random.choice(string.ascii_letters))
    elif(flag == 0 & contador != numero):
        Arreglo_aleatorio1.append(x)
        flag == 1
    else:
        Arreglo_aleatorio1.append(y)
    contador = contador + 1

# SE DEFINEN LAS FUNCIONES PARA CORRER PRUEBAS DE PYTEST


def test_answer1():
    assert multiple_op(x) == [x*x, pow(2, x), math.factorial(x)]
    # CASO DE EXITO DE MULTIPLE_OP


def test_answer2():
    assert multiple_op(random.choice(string.ascii_letters)) == 805
    # CASO DE FALLO DE MULTIPLE OP SE LLAMA CON STRING EN ARGUMENTO


def test_answer3():
    assert verify_array_op(A_A) == [
        [A_A[0]*A_A[0], pow(2, A_A[0]), math.factorial(A_A[0])],
        [A_A[1]*A_A[1], pow(2, A_A[1]), math.factorial(A_A[1])],
        [A_A[2]*A_A[2], pow(2, A_A[2]), math.factorial(A_A[2])]
        ]
    # CASO DE EXITO DE VERIFY_ARRAY_OP


def test_answer4():
    assert verify_array_op(Arreglo_aleatorio1) == 508
    # CASO DE FALLO DE VERIFY_ARRAY_OP CON STRING EN LISTA DE ARGUMENTO

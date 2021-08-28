# TAREA 2: KARINA AZOFEIFA ADRIAN OROZCO
# SE IMPORTAN LAS LIBRERIAS A UTILIZAR
# ARGPARSE IMPLEMENTADA SEGUN REQUISITO DE TAREA
import argparse
# RANDOM USADA PARA LLENAR ARRAY DE ELEMENTOS ALEATORIOS
import random
# TIMEIT USADA PARA MEDIR TIEMPO DE EJECUCION
import timeit
# THREADING PARA HABILIAR PROGRAMACION POR HILOS
import threading
# LOGGING FUE USADA PARA OBTENER INFO DE HILOS
import logging
# SYS USADA PARA LLAMAR FUNCION EN SHELL
import sys

global Arreglo
global numero
global formato
numero = 0
Arreglo = []
# LOGGING USADO PARA OBTENER INFO DE THREADS
# DURANTE PROCESO DE DEBUG
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
# SE DEFINE FUNCION MAIN
# USADA PARA CONFIGURACION DE ARGPARSE


def main():
    parser = argparse.ArgumentParser()
    # SE DECLARAN PARAMETROS DE FUNCION
    # EN CASO DE NO RECIBIR PARAMETROS SE EJECUTA LA FUNCION
    # USANDO VALORES POR DEFECTO CON FINES DEMOSTRATIVOS
    parser.add_argument('-X', type=int, default=2000000,
                        help='Ingrese el numero de datos del arreglo')
    parser.add_argument('-formato', default=1, type=int,
                        help='Ingrese 1 para impresion en pantalla y 0 para impresion en txt(Opcional)')
    # SE AGREGAN ARGUMENTOS A LA LISTA
    args = parser.parse_args()
    # SE LLAMA LA FUNCION ARRAY POTENCIAS
    # USANDO LOS ARGUMENTOS RECOPILADOS
    sys.stdout.write(str(Array_Potencias(args.X, args.formato)))
# FUNCION POTENCIA
# RECIBE UNA LISTA DE ELEMENTOS
# CALCULA LA POTENCIA DE CADA ELEMENTO
# USADA PARA LOS CALENDARIZACION DE THREADS


def Potencia(lista):
    contador = 0
    while contador < len(lista):
        potencia = pow(lista[contador], 2)
        contador = contador + 1
    return 1
# FUNCION ARRAY_POTENCIAS
# RECIBE CANTIDAD DE ELEMENTOS EN ARRAY
# RECIBE FORMATO DE IMPRESION DE RESULTADOS


def Array_Potencias(X, formato):
    # SI FORMATO==0 SE HACE IMPRESION EN ARCHIVO TXT
    if(formato == 0):
        # SE INICIALIZA CONTADOR DE CONTROL
        contador = 0
        # SIZE USADA PARA GENERAR ARRAY DE ELEMENTOS
        size = X
        # SE ABRE EL ARCHIVO DONDE SE ESCRIBEN RESULTADOS
        f = open('Registrodetiempo.txt', 'w')
        # VARIABLE DONDE SE ESCRIBEN RESULTADOS DE POTENCIA
        resultado = 0
        # SE VERIFICA QUE X SEA UN NUMERO ENTERO
        if(type(X) != int):
            # CODIGO DE ERROR 805: ARGUMENTOS DE ENTRADA INVALIDOS
            return 805
        # SE VERIFICA QUE FORMATO SEA NUMERO ENTERO
        elif(type(formato) != int):
            return 805
        # CICLO USADO PARA LLENAR DE NUMEROS ALEATORIOS EL ARRAY
        while size != 0:
            Arreglo.append(random.randint(100, 200))
            size = size-1
        # POR DEFECTO, PYTHON CORRE EL PROGRAMA EN UNICO HILO
        # COMIENZA MEDICION PARA EJECUCION EN HILO UNICO
        # SE MIDE CON VARIABLE DE INICIO
        inicio = timeit.default_timer()
        # CICLO FOR AVANZA ELEMENTO POR ELEMENTO Y CALCULA POTENCIA
        for elemento in Arreglo:
            resultado = pow(elemento, 2)
        # UNA VEZ SE RECORREN TODOS LOS ELEMENTOS SE MIDE EL TIEMPO EN FIN
        fin = timeit.default_timer()
        # FORMATO DE ESCRITURA EN TXT
        f.write('Tiempo con hilo único')
        f.write('\n')
        # SE ESCRIBE LA DIFERENCIA ENTRE INICIO Y FIN
        # REPRESENTA EL TIEMPO DE EJECUCION
        f.write(str(fin-inicio))
        # SE REINICIAN VARIABLES DE MEDICION DE TIEMPO
        inicio = 0
        fin = 0
        # COMIENZA ALGORITMO MULTIHILO
        # PRIMERO SE HACE DIVISION ENTERA
        # SE OBTIENE CANTIDAD DE ELEMENTOS A REPARTIR EN CADA THREAD
        division = X//4
        # RESIDUO INDICA ELEMENTOS QUE PUEDEN SOBRAR
        # EN CASO DE QUE X NO SEA MULTIPLO DE 4
        residuo = X % 4
        # SE DEFINEN LISTAS QUE PROCESARAN LOS THREADS
        lista_thread_1 = Arreglo[:division]
        lista_thread_2 = Arreglo[division+1:2*division]
        lista_thread_3 = Arreglo[(2*division)+1: 3*division]
        lista_thread_4 = Arreglo[(3*division)+1:4*division]
        # EN CASO DE HABER RESIDUO SE REPARTEN LOS ELEMENTOS
        if(residuo == 3):
            lista_thread_1.append(Arreglo[X-1])
            lista_thread_2.append(Arreglo[X-2])
            lista_thread_3.append(Arreglo[X-3])
        if(residuo == 2):
            lista_thread_1.append(Arreglo[X-1])
            lista_thread_2.append(Arreglo[X-2])
        if(residuo == 1):
            lista_thread_1.append(Arreglo[X-1])
        # SE DECLARAN 4 THREADS UNICOS QUE PROCESARAN DATOS
        # CADA THREAD RECIBE LA LISTA CREADA Y USAN LA FUNCION POTENCIA
        thread_1 = threading.Thread(target=Potencia, args=(lista_thread_1, ))
        thread_2 = threading.Thread(target=Potencia, args=(lista_thread_2, ))
        thread_3 = threading.Thread(target=Potencia, args=(lista_thread_3, ))
        thread_4 = threading.Thread(target=Potencia, args=(lista_thread_4, ))
        # SE INICIA EJECUCION DE THREADS
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
        # SE COMIENZA A MEDIR EL TIEMPO EN EL QUE SE PROCESAN LOS DATOS
        # CON COMANDO JOIN
        # SE ESPERA A QUE EL PROCESAMIENTO DE DATOS ACABE EN LOS THREADS
        inicio_4_hilos = timeit.default_timer()
        thread_1.join()
        thread_2.join()
        thread_3.join()
        thread_4.join()
        fin_4_hilos = timeit.default_timer()
        # SE MIDE TIEMPO FINAL
        # SE OBTIENE TIEMPO DE EJECUCION
        tiempo = fin_4_hilos-inicio_4_hilos
        # SE AGREGAN LOS RESULTADOS AL TXT
        f.write('\n')
        f.write('Tiempo con 4 hilos')
        f.write('\n')
        f.write(str(tiempo))
        # SE REINICIAN VARIABLES DE MEDICION
        inicio_4_hilos = 0
        fin_4_hilos = 0
        # SE CIERRA ARCHIVO TXT
        f.close()
        # SE INDICA AL USUARIO QUE ACABA PROCESO
        print('Operación Exitosa')
    else:
        # LA LOGICA USADA ES IDENTICA AL CASO ANTERIOR
        # EN ESTE CASO LO QUE CAMBIA ES EL FORMATO DE IMPPRESION
        # EN VEZ DE ESCRIBIR RESULTADOS EN TXT
        # SE IMPRIMEN EN SHELL
        # VARIABLES DE CONTROL
        size = X
        contador = 0
        resultado = 0
        # LOGICA DE VERIFICACION
        if(type(X) != int):
            # CODIGO DE ERROR 805: ARGUMENTOS DE ENTRADA INVALIDOS
            return 805
        elif(type(formato) != int):
            return 805
        # SE ARMA ARRAY
        while size != 0:
            Arreglo.append(random.randint(100, 200))
            size = size-1
        # SE MIDE TIEMPO DE EJECUCION HILO UNICO
        inicio = timeit.default_timer()
        while contador < X:
            resultado = pow(Arreglo[contador], 2)
            contador = contador + 1
        fin = timeit.default_timer()
        # SE IMPRIMEN RESULTADOS
        print("Tiempo con hilo único")
        print("\n")
        print(fin-inicio)
        inicio = 0
        fin = 0
        # LOGICA MULTIHILO
        # APLICA MISMA LOGICA QUE CASO ANTERIOR
        division = X//4
        residuo = X % 4
        lista_thread_1 = Arreglo[:division]
        lista_thread_2 = Arreglo[division+1:2*division]
        lista_thread_3 = Arreglo[(2*division)+1: 3*division]
        lista_thread_4 = Arreglo[(3*division)+1:4*division]
        if(residuo == 3):
            lista_thread_1.append(Arreglo[X-1])
            lista_thread_2.append(Arreglo[X-2])
            lista_thread_3.append(Arreglo[X-3])
        if(residuo == 2):
            lista_thread_1.append(Arreglo[X-1])
            lista_thread_2.append(Arreglo[X-2])
        if(residuo == 1):
            lista_thread_1.append(Arreglo[X-1])
        thread_1 = threading.Thread(target=Potencia, args=(lista_thread_1, ))
        thread_2 = threading.Thread(target=Potencia, args=(lista_thread_2, ))
        thread_3 = threading.Thread(target=Potencia, args=(lista_thread_3, ))
        thread_4 = threading.Thread(target=Potencia, args=(lista_thread_4, ))
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
        # SE MIDE TIEMPO DE EJECUCION
        inicio_4_hilos = timeit.default_timer()
        thread_1.join()
        thread_2.join()
        thread_3.join()
        thread_4.join()
        fin_4_hilos = timeit.default_timer()
        tiempo = fin_4_hilos-inicio_4_hilos
        # SE IMPRIMEN RESULTADOS
        print("\n")
        print("Tiempo con 4 hilos")
        print("\n")
        print(tiempo)
        inicio_4_hilos = 0
        fin_4_hilos = 0
# INSTANCIACION DE MAIN PARA EJECUTAR EN SHELL


if __name__ == '__main__':
    main()

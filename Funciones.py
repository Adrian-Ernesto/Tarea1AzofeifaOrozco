# TAREA 1 - MT7003
# ADRIAN OROZCO RIVERA- KARINA AZOFEIFA AMPIE


# FUNCION MULTIPLE_OP REALIZA MULTIPLICACION, POTENCIA EN BASE 2 Y FACTORIAL
# ENTRADA: NUMERO ENTERO
# SALIDA: ARREGLO DE NUMEROS
def multiple_op(x):
    # SE DECLARA VARIABLE ARREGLO PARA LA SALIDA
    Arreglo = []
    # SE DECLARA CONTADOR DE CONTROL
    contador = 1
    # SE DECLARA VARIABLE FACTORIAL PARA GENERAR TERCER ELEMENTO DE LA LISTA
    factorial = 1
    # PRIMERO SE VERIFICA QUE EL TIPO DE DATO ES VALIDO CON UN CONDICIONAL
    if(type(x) != int):
        # CODIGO DE ERROR UNICO 805: TIPO DE DATO INVALIDO
        return 805
    else:
        # EL PRIMER APPEND GENERA EL ELEMENTO X*X EN LA SALIDA
        Arreglo.append(x*x)
        # SE USA POW PARA AGREGAR EL SEGUNDO ELEMENTO INDICADO A LA SALIDA
        Arreglo.append(pow(2, x))
        # CON UN CICLO WHILE SE GENERA EL FACTORIAL PARA EL ARREGLO DE SALIDA
        while (contador <= x):
            factorial = factorial * contador
            contador = contador + 1
        else:
            # SE AGREGA EL FACTORIAL A LA SALIDA
            Arreglo.append(factorial)
            # SE RETORNA EL ARREGLO DE SALIDA
            return Arreglo

# FUNCION VERIFY_ARRAY_OP PARA GENERAR ARREGLO DE ARREGLOS USANDO MULTIPLE_OP
# ENTRADA: UN ARREGLO DE NUMEROS
# SALIDA: UN ARREGLO DE ARREGLOS


def verify_array_op(Arreglo):
    # SE DECLARA VARIABLE RESULTADO PARA LA SALIDA
    Resultado = []
    # SE DECLARA CONTADOR DE CONTROL
    contador = 0
    while(contador < 3):
        # PARA CADA ELEMENTO DE LA LISTA SE VALIDA EL TIPO DE DATO
        if(type(Arreglo[contador]) != int):
            # CODIGO DE ERROR UNICO 508: DATO INVALIDO EN LISTA
            return 508
        else:
            # PARA DATOS VALIDOS SE USA MULTIPLE_OP PARA AGREGAR
            # LISTA AL ARREGLO DE SALIDA
            Resultado.append(multiple_op(Arreglo[contador]))
            contador = contador + 1
    # SE RETORNA ARREGLO DE ARREGLOS COMO SALIDA
    return Resultado

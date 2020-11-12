# Variables globales
la_palabra_o_caracter_contiene_validacion_lexica = False

def verificar_si_es_comentario(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.startswith('#') and len(palabra_o_caracter) > 1:
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un comentario'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_operadores_aritmeticos(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.__eq__('+'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de adicion'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('-'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de subtraccion'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('*'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de multiplicacion'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('/'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de division'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('%'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de modulo'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('**'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de exponente'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('//'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador aritmetico de divison de piso'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_operadores_de_comparasion(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.__eq__('=='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de igualdad'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('!='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de desigualdad'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('<>'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de desigualdad para dos operandos'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('>'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de mayor que'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('<'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de menor que'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('>='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de mayor o igual que'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('<='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de comparacion de menor o igual que'.format(palabra_o_caracter=palabra_o_caracter))



def verificar_operadores_de_asignacion(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.__eq__('='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('+='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de suma'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('-='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de resta'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('*='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de multiplicacion'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('/='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de division'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('%='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de modulo'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('**='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de exponente'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('//='):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de asignacion de division de piso'.format(palabra_o_caracter=palabra_o_caracter))



def verificar_operadores_logicos(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.__eq__('and'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador logico'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('AND'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador logico'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('or'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador logico'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('OR'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador logico'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('not'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador logico'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('NOT'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador logico'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_operadores_de_membresia(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.__eq__('in'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de membresia'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('not_in'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de membresia'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_operadores_de_identidad(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.__eq__('is'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de identidad'.format(palabra_o_caracter=palabra_o_caracter))
    elif palabra_o_caracter.__eq__('is_not'):
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un operador de identidad'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_palabras_reservadas(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    palabras_reservadas = [
        'and', 'except', 'lambda', 'with', 'as', 'finally', 'nonlocal', 'while', 'assert', 'False', 'None', 'yield',
        'break', 'for', 'not', 'class', 'from', 'or', 'continue', 'continue', 'global', 'pass', 'def', 'if', 'raise',
        'del', 'import', 'return', 'elif', 'in', 'True', 'else', 'is', 'try'
    ]

    if palabra_o_caracter in palabras_reservadas:
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es una palabra reservada'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_numeros(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.isnumeric():
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: es un numero'.format(palabra_o_caracter=palabra_o_caracter))


def verificar_si_la_palabra_o_caracter_pertenece_al_abecedario(palabra_o_caracter):
    # se declara que la variable 'la_palabra_contiene_validacion_lexica' es de tipo global para acceder a su contenido
    global la_palabra_o_caracter_contiene_validacion_lexica

    if palabra_o_caracter.isalpha():
        la_palabra_o_caracter_contiene_validacion_lexica = True
        print('{palabra_o_caracter}: pertenece al abecedario'.format(palabra_o_caracter=palabra_o_caracter))

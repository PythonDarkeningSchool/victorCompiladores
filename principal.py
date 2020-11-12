import verificaciones

# Variables globales
entrada_usuario = ""


def realizar_verificaciones_lexicas(palabra_o_caracter_ingresado):
    verificaciones.verificar_si_es_comentario(palabra_o_caracter_ingresado)
    verificaciones.verificar_operadores_aritmeticos(palabra_o_caracter_ingresado)
    verificaciones.verificar_operadores_de_comparasion(palabra_o_caracter_ingresado)
    verificaciones.verificar_operadores_de_asignacion(palabra_o_caracter_ingresado)
    verificaciones.verificar_operadores_logicos(palabra_o_caracter_ingresado)
    verificaciones.verificar_operadores_de_membresia(palabra_o_caracter_ingresado)
    verificaciones.verificar_operadores_de_identidad(palabra_o_caracter_ingresado)
    verificaciones.verificar_palabras_reservadas(palabra_o_caracter_ingresado)
    verificaciones.verificar_numeros(palabra_o_caracter_ingresado)


def procesar_entrada_usuario():
    # PASO 1: creamos una lista con las palabras o caracteres ingresados por el usuario
    lista_de_palabras_ingresadas = entrada_usuario.split()

    for palabra_o_caracter_ingresado in lista_de_palabras_ingresadas:
        # PASO 2: por cada palabra o caracter ingresado se van a realizar las validaciones lexicas
        realizar_verificaciones_lexicas(palabra_o_caracter_ingresado)

        # PASO 3 (opcional): Si la palabra o caracter ingresado no pasa las validaciones lexicas, se haran validaciones por cada caracter
        # en la palabra o caracter actual en el ciclo del for
        if not verificaciones.la_palabra_o_caracter_contiene_validacion_lexica:
            for caracter in palabra_o_caracter_ingresado:  # iterando sobre cada caracter para hacer las validaciones lexicas de nuevo
                # PASO 4 (opcional): Se realizan de nuevo las validaciones lexicas anteriores para cada caracter
                realizar_verificaciones_lexicas(caracter)
                # PASO 5 (opcional): Se realiza una nueva validacion para ver si el caracter pertenece al abecedario
                verificaciones.verificar_si_la_palabra_o_caracter_pertenece_al_abecedario(caracter)

                # PASO 6 (opcional): si el caracter actual no contiene una validacion lexica, se mostrara un mensaje de error
                if not verificaciones.la_palabra_o_caracter_contiene_validacion_lexica:
                    print('(error) {caracter}: no contiene validacion lexica!'.format(caracter=caracter))

                # Se restaura la validacion lexica para la siguiente palabra
                verificaciones.la_palabra_o_caracter_contiene_validacion_lexica = False


def leer_entrada_usuario():
    global entrada_usuario  # se declara que la variable 'entrada_usuario' es de tipo global para acceder a su contenido
    entrada_usuario = input("Por favor inserte una palabra o un caracter: ")

    # Si el usuario no teclea un valor, se le seguira preguntando hasta que inserte un valor
    while entrada_usuario == "":
        entrada_usuario = input("Por favor inserte una palabra o un caracter: ")


if __name__ == '__main__':
    # Si el programa se manda a llamar desde linea de comando 'python principal.py' entrara a esta funcion
    leer_entrada_usuario()
    procesar_entrada_usuario()

# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
# - Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
# (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)


# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.



#funcion sin retorno
def saludo():
    print("Hola, soy una funcion sin retorno")


#funcion con retorno
def otro_saludo():
    return "Hola, soy una funcion con retorno"


#funcion con arguntos y retorno
def saludo_con_arguntos (name):
    return f"Hola soy {name}, y soy una funcion con agrumentos y retorno"


#funcion con parametros por defecto
def saludo_default(default_name = "me llamo Python"):
    return f"Hola yo soy una funcinon con parametros por defecto y mi nombre es {default_name}"


# Con retorno de varios valores
def saludo_multiple():
    return "Hola", "Python"


# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

        # Con un número variable de argumentos con palabra clave


def variable_key_arg_greet(**persona):
    for key, value in persona.items():
        print(f"{key}: {value}")



#programa principal
saludo()


print(otro_saludo())


saludo_con_argumento =saludo_con_arguntos("Andres")
print(saludo_con_argumento)


saludo_def = saludo_default()
print(saludo_def)


greet, name =saludo_multiple()
print(greet)
print(name)


variable_arg_greet("Andres", "Luis", "Pablo", "Maria")


variable_key_arg_greet(
    Nombre="Andres",
    Apellidos="Cecconi",
    Cursos="Python",
    Lenguajes="Python, Javascript, Html, Css",
    Edad=33,
)



"""
Ejercicio Extra
"""

def funcion (text_1, text_2)-> int:
    contador = 0
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{text_1} {text_2}")
        elif i % 5 == 0:
            print(text_2)
        elif i % 3 == 0:
            print(text_1)
        else:
            print(i)
        contador += 1
    return contador

funcion("Hello", "World")


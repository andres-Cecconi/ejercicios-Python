"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

"""

#listas
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista)
# print(type(lista))
# print(len(lista))
# print(max(lista))  
# print(min(lista))

# lista.append(11)
# lista.pop(4)
# lista.insert(0, 15)
# lista.sort()
# print(lista)



#tuplas
# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(tupla)
# print(type(tupla))
# print(len(tupla))
# print(max(tupla))  
# print(min(tupla))

#tupla.append(11)
#print(tupla)   ---> Esto no se puede hacer. la diferencia central entre una lista y una tupla es su inmutabilidad. No es posible modificar una tupla


#diccionarios

# diccionario = { "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10 }
# print(diccionario)
# print(type(diccionario))
# print(len(diccionario))
# print(max(diccionario))  
# print(min(diccionario))
# print("uno" in diccionario)

# diccionario["once"] = 11
# print(diccionario)

#Un diccionario es una lista de pares clave-valor. Por ejemplo, la clave 'uno' tiene el valor 1 y la clave 'dos' tiene el valor 2. 

"""
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización  y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.

"""

agenda = {}

while True:
    print("¿Que operación deseas realizar?")
    print("1. Buscar")
    print("2. Insertar")
    print("3. Actualizar")  
    print("4. Eliminar")
    print("5. Mostrar contactos")
    print("6. Salir")
    operacion = int(input())
    if operacion == 1:
        print("¿Que contacto deseas buscar?")
        nombre = input()
        if nombre in agenda:
            print(f"El contacto {nombre} tiene el teléfono {agenda[nombre]}")
        else:
            print(f"El contacto {nombre} no existe")
    elif operacion == 2:
        print("¿Que contacto deseas insertar?")
        nombre = input()
        if nombre not in agenda:
            print("Introduce el teléfono del contacto")
            tel = input()
            agenda[nombre] = tel
            print("Contacto insertado")
        else:
            print("El contacto ya existe")
    elif operacion == 3:  
        print("¿Que contacto deseas actualizar?")
        nombre = input()
        if nombre in agenda:
            print("Introduce el nuevo telfono del contacto")
            tel = input()
            agenda[nombre] = tel
            print("Contacto actualizado")
        else:
            print("El contacto no existe")
    elif operacion == 4:
        print("¿Que contacto deseas eliminar?")
        nombre = input()
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado")
        else:
            print("El contacto no existe")
    elif operacion == 5:    
        print("Contactos:")
        for nombre, tel in agenda.items():
            print(f"{nombre}: {tel}")
    elif operacion == 6:
        print("Saliendo...")
        print("Gracias por usar la agenda de contactos")
        break
    else:
        print("Operación no disponible")

'''
En una veterinaria se requiere una pequeña interfaz por línea de comandos que permita:

Opción 1: Cargar un archivo csv con datos de 5 mascotas. Tras una persona seleccionar esta opción, debe el sistema indicar un mensaje "Se cargaron los datos de 5 mascotas".
Opción 2: Mostrar datos de mascotas cargadas en el sistema.
Opción 3: Agregar mascota. En esta opción el sistema solicita los datos de la mascota para su registro.
Opción 4: Buscar mascota. Al seleccionar esta opción, el sistema indicar subopciones de búsqueda como: nombre mascota, dueño, raza, edad o DNI. Acorde a la opción y valor ingresado se debe mostrar las mascotas que cumplen dichos criterios.
Opción 5: Ordenar mascota. Al seleccionar esta opción, el sistema indicar subopciones de ordenamiento como: nombre mascota, dueño, raza, edad o DNI. Acorde a la opción y valor ingresado se debe mostrar las mascotas que cumplen dichos criterios.
Opción 6: Guardar mascotas en archivo de disco duro (.txt o csv)

Se solicita escribir un programa en Python que permita realizar las gestiones descritas en las opciones líneas arriba. 
Para ello, se debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python. 

'''
import pandas as pd
import csv
import random  # Importamos la librería random
import sys  #para finalizar el juego
import time  #para definir tiempo
from csv import writer
#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
time.sleep(1)  # Espera 1 segundos antes de continuar.
print(CYAN +"=== Bienvenido la veterinaria Kolitas=== ")
print("=== Elija una de las opciones diponibles ===\n" +RESET)
time.sleep(1)  # Espera 1 segundos antes de continuar.
def menu():
    print(YELLOW+ "presione 1 para  cargar datos de su mascota ")
    print("presione 2 para mostrar los datos de mascotas cargadas en el sistema")
    print("presione 3 para agregar mascota")
    print("presione 4 para buscar mascota")
    print("presione 5 para ordenar mascota")
    print("presione 6 para guardar mascotas \n" +RESET)
    opcion = int(input("Elija una opcion correcta: "))
    while opcion not in (1,2,3,4,5,6):
            opcion = input("la opcion no existe, elija una opcion correcta: ")
    if opcion == 3:
        agregar_mascota()
    if opcion == 4:
        buscar_mascota()

def agregar_mascota():
    print("Necesitamos los siguientes datos de la mascota para su registro")
    nombre_mascota=input("Nombre mascota: ")
    nacimiento_mascota=input("Ingrese Dia, Mes y Año de nacimiento"
                    "(Separados por un guion slash / ): ")
    raza_mascota=input("raza Mascota: ")
    nombre_dueño=input("nombre del dueño: ")
    identificacion_Dni=int(input("identificacion: ")[0:8])
    list_add = [nombre_mascota,nacimiento_mascota,raza_mascota,nombre_dueño,identificacion_Dni]
    #agregar datos al archivo CSV
    #csvwriter_object.writerow(list_add)
    with open('registro.csv', 'a', encoding= "utf-8",newline='') as f_object:  
    # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
    # Result - a writer object
    # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(list_add)  
    # Close the file object
        f_object.close()
      
def buscar_mascota():
    archivo = pd.read_csv('registro.csv', encoding = 'utf-8')
    print("1. Buscar nombre de mascota")
    print("2. Buscar dueño de mascota")
    print("3. Buscar raza de la mascota")
    print("4. Buscar edad de mascota")
    print("5. Buscar por DNI del dueño")
    opcion_2 = int(input("Elija una opcion correcta: "))
    if opcion_2 == 1:
        buscar = input('buscar: ')
        encontrar = archivo.query('nombre == @buscar ')
        if encontrar.empty:
            print("noup")
        else :
            print(encontrar)
menu()
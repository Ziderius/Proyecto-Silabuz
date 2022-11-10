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

import csv
import time
from tqdm import tqdm 
    #módulo tqdm progress bar: pip install tqdm

# Abrir y leer csv
class Veterinaria:
    def __init__(self, reg = "registro.csv"):
        self.reg = reg
        self.listas = []
        with open(self.reg, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.listas.append(row)
            self.fieldnames = ['nombre', 'nacimiento', 'raza', 'dueño', 'dni']          

    # Menú de opciones
    def menu(self):
        opc = 0
        while opc != 1:
            print('''
            ¡Bienvenido al Sistema de Registro Veterinario!
            Menú de opciones
            1 : Cargar archivo de registro.
            ''')
            time.sleep(1)
            opc = int(input("Introduzca su opción: "))
            if opc == 1:
             self.carga()

    # Cargardo archivo
    def carga(self):
        print("\nIniciando carga, por favor, espere.")
        data =[]
        pbar = tqdm(total=100)
        for i in range(20):
            time.sleep(0.1)
            pbar.update(5)
            pbar.set_description("Cargando archivo...")
        pbar.close()
        print("Archivo cargado con éxito.\n")

Vet = Veterinaria()
Vet.menu()
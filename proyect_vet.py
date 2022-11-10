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
import pandas as pd
# módulo pandas: pip install pandas
import time
from tqdm import tqdm 
# módulo tqdm progress bar: pip install tqdm

# Abrir y leer csv
class Veterinaria:
    def __init__(self, reg = "registro.csv"):
        self.reg = reg
        self.listas = []
        with open(self.reg, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.listas.append(row)
            self.fieldnames = ['Nombre', 'Nacimiento', 'Raza', 'Dueño', 'DNI']          

    # Menú de opciones
    def menu(self):
        opc = 0
        while opc != 3:
            print('''
            ¡Bienvenido al Sistema de Registro Veterinario!
            Menú de opciones
            1 : Cargar archivo de registro.
            2 : Mostrar datos de mascotas registradas.
            3 : Añadir nuevo registro de mascota.
            ''')
            time.sleep(1)
            opc = int(input("Introduzca su opción: "))
            if opc == 1:
                self.carga()
            if opc == 2:
                self.datos()
            if opc == 3:
                self.agregar()

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
    
    # Mostrar y listar datos
    def datos(self):
        print("\nIniciando lista de registro de mascotas...\n")
        time.sleep(2)
        mascotas = pd.read_csv(self.reg, encoding="utf-8")
        print(mascotas)
        time.sleep(1)
        print("\nProceso finalizado.")
    
    # Añadir mascotas con los datos del registro
    def agregar(self):
        print("\nIniciando opción de añadir mascota...")
        time.sleep(2)
        print("Por favor, escriba lo que el sistema le solicite:\n")
        time.sleep(2)
        count = len(self.listas)
        nombre = input("Ingrese nombre de la mascota: ")
        time.sleep(1)
        nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AA): ")
        time.sleep(1)
        raza = input("Ingrese raza de la mascota: ")
        time.sleep(1)
        own = input("Ingrese nombre del dueño: ")
        time.sleep(1)
        dni = input("Ingrese número de DNI del dueño: ")
        while dni.isdigit() != True:
            print("El dato ingresado es incorrecto, vuelva a intentarlo.")
            dni = input("Ingrese número de DNI del dueño: ")
        time.sleep(1)
        print("\nDatos añadidos correctamente.")
        agr = {'Nombre': nombre.capitalize(), 'Nacimiento': nacimiento, "Raza": raza.capitalize(), "Dueño": own.capitalize(), "DNI": dni}
        self.listas.append(agr)
        with open(self.reg, 'w', encoding="utf-8", newline='') as file:
            agrega = csv.DictWriter(file, fieldnames=self.fieldnames)
            agrega.writeheader()
            agrega.writerows(self.listas)

Vet = Veterinaria()
Vet.menu()
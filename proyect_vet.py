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
from time import sleep
from tqdm import tqdm
import pandas as pd


class veterinaria:
    def menu(self):
        opcion = 0
        while opcion != 2:
            print("1.Cargar archivo: ")
            print("2.Mostrar datos: ")
            opcion = int(input("Elige tu opción: "))
            if opcion == 1:
                self.cargar()
            if opcion == 2:
                self.mostrar()

    def cargar(self):
        archivo = pd.read_csv("registro.csv", encoding='utf-8')
        mascotas = pd.DataFrame(archivo)
        mascotas = len(mascotas)
        
        print("Cargando datos...")

        for i in tqdm (range (100), desc="Cargando…", ascii=False, ncols=75):
            sleep(0.01)

        print(f"Se han cargado los datos de {mascotas} mascotas")

    def mostrar(self):
        archivo = pd.read_csv("registro.csv", encoding='utf-8')
        print(archivo)
         

vet = veterinaria()
vet.menu()

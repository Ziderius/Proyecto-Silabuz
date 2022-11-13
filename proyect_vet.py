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

class veterinaria:
    def menu(self):
        opcion = 0
        while opcion != 2:
            print("1.Cargar archivo: ")
            opcion = int(input("Elige tu opción: "))
            if opcion == 1:
                self.cargar()
            if opcion == 2:
                self.mostrar()

    def cargar(self):
 
        print("Cargando datos...")

        for i in tqdm(range(10)):
            sleep(1)

        print("Se han cargado los datos de 6 mascotas.")

 #   def mostrar(self):






vet = veterinaria()
vet.menu()

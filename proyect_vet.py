import csv
import pandas as pd
# módulo pandas: pip install pandas
import time
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
        while opc != 7:
            print('''
            ¡Bienvenido al Sistema de Registro Veterinario!
            5 : Ordenar mascotas por datos de registro.
            6 : Guardar los datos.
            7 : Salir. 
            ''')
            time.sleep(1)
            opc = int(input("Introduzca su opción: "))
            if opc == 5:
                self.ordena()
            if opc == 6:
                self.guardar()
            if opc == 7:
                self.salir()
            else:
                print("Elección no válda. Intente de nuevo.")    

    def ordena(self):
        pass

    def guardar(self):
        pass

    def salir(self):
        pass

vet = Veterinaria()
vet.menu()
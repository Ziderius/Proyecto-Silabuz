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
        while opc != 5:
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
            if opc == 4:
                self.busq()
            if opc == 5:
                self.salir()
            else:
                exit()

    # Cargardo archivo
    def carga(self):
        print("\nIniciando carga, por favor, espere.")
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
    
    # Añadir mascotas con datos del registro
    def agregar(self):
        print("\nIniciando opción de añadir mascota...")
        time.sleep(2)
        print("Por favor, escriba lo que el sistema le solicite:\n")
        time.sleep(2)
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
            print("El dato es errado, vuelva a intentarlo.")
            dni = input("Ingrese número de DNI del dueño: ")
            
        time.sleep(1)
        print("\nDatos añadidos correctamente.")
        agr = {'Nombre': nombre.capitalize(), 'Nacimiento': nacimiento, "Raza": raza.capitalize(), "Dueño": own.capitalize(), "DNI": dni}
        self.listas.append(agr)
        with open(self.reg, 'w', encoding="utf-8", newline='') as file:
            escr = csv.DictWriter(file, fieldnames=self.fieldnames)
            escr.writeheader()
            escr.writerows(self.listas)
  
    # Búsqueda de datos de mascotas según registro
    def busq(self):
        print("Iniciando submenú de búsqueda...")
        time.sleep(2)
        opc_busq = 0
        registro = self.reg
        while opc_busq != 1:
            print("1 : Nombre de mascota.")
        opc_busq = input("Ingrese su opción: ")
        if opc_busq == "1":
            resul_opc = input("Ingrese nombre de la mascota: \n")
            for i in registro:
                if i["Nombre"] == resul_opc:
                    print(f"Nacimiento: {i['Nacimiento']}")

    def salir(self):
        pass

vet = Veterinaria()
vet.menu()

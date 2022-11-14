import pandas as pd
import csv
from time import sleep
from csv import writer
from datetime import datetime
from tqdm import tqdm

# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Programa 
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
        while opc != 8:
            print(MAGENTA+'''
            ¡Bienvenido al Sistema de Registro Veterinario!

            - Menú principal -
            1 : Cargar registro de mascotas.
            2 : Mostrar datos de las mascotas registradas.
            3 : Agregar nueva mascota.
            4 : Submenú de búsqueda por dato registrado.
            5 : Ordenar registro por dato.
            6 : Guardar registro en un nuevo archivo.
            7 : Salir
            '''+ RESET)
            opc = int(input(CYAN+ "Introduzca su opción: "+RESET))
            if opc == 1:
                self.cargar()
            if opc == 2:
                self.mostrar()
            if opc == 3:
                self.agregar_mascota()
            if opc == 4:
                self.buscar_mascota()
            if opc == 5:
                self.ordern()
            if opc == 6:
                self.guardar()
            if opc == 7:
                self.salir()
        else:
            print(RED+"Elección no válida. Regresando al menú principal."+RESET)
            sleep(2)
            return self.menu()

    def cargar(self):
        archivo = pd.read_csv("registro.csv", encoding='utf-8')
        mascotas = pd.DataFrame(archivo)
        mascotas = len(mascotas)
        print(BLUE+"Cargando datos...")
        for i in tqdm (range (100), desc="Cargando…", ascii=False, ncols=75):
            sleep(0.01)
        print(f"Se han cargado los datos de {mascotas} mascotas")
        sleep(2)
        
    def mostrar(self):
        archivo = pd.read_csv("registro.csv", encoding='utf-8')
        print(archivo)
        sleep(3)

    # agregar mas mascotas al archivo CSV
    def agregar_mascota(self):
        print("Necesitamos los siguientes datos de la mascota para su registro")
        nombre_mascota=input("Nombre mascota: ")
        nacimiento_mascota=input("Ingrese Dia, Mes y Año de nacimiento (Separados por un guion slash '/'): ")
        raza_mascota=input("raza Mascota: ")
        nombre_dueño=input("nombre del dueño: ")
        identificacion_Dni=(input("DNI: "+RESET)[0:8])
        while identificacion_Dni.isdigit() != True:
            print("Solo se aceptan números hasta de 8 dígitos")
            identificacion_Dni=(input("DNI: "+RESET)[0:8])

        list_add = [nombre_mascota.capitalize(),nacimiento_mascota,raza_mascota.capitalize(),nombre_dueño.capitalize(),identificacion_Dni]
        with open('registro.csv', 'a', encoding= "utf-8",newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow(list_add)  
            f_object.close()

    # buscar datos de el archivo CSV
    def buscar_mascota(self):
        sleep(1.5)
        archivo = pd.read_csv('registro.csv', encoding = 'utf-8')
        print(MAGENTA+'''

            - Submenú de búsqueda -
            1 : Buscar nombre de mascota.
            2 : Buscar dueño de mascota.
            3 : Buscar raza de la mascota.
            4 : Buscar edad de mascota.
            5 : Buscar por DNI del dueño.
            '''+ RESET)
        sleep(1)
        opcion_2 = int(input("Elija una opcion correcta: "))
        if opcion_2 == 1:
            buscar = input('Buscar: ')
            encontrar = archivo.query('Nombre == @buscar')
            if encontrar.empty:
                sleep(1.5)
                print("No se encontraron datos.")
                sleep(2.5)
            else :
                print(encontrar)
                sleep(2.5)
        
    # Submenú de ordenamiento por lo que el usuario requiera
    def ordern(self):
        datosVet = self.listas
        opc_busq = 0
        while opc_busq != 7:
            sleep(1.5)
            print(MAGENTA+'''
            - Submenú de ordenamiento del registro veterinario -
 
            1 : Ordenar por Nombre de mascota
            2 : Ordenar por Edad
            3 : Ordenar por Raza
            4 : Ordenar por Dueño
            5 : Ordenar por DNI
            6 : Retornar al menú principal
            7 : Salir del programa'''+RESET)
            sleep(1)
            opc_busq = int(input(CYAN+"\nIngrese su opción: "+RESET))
            sleep(2)

            if opc_busq == 1:
                datosVet.sort(key = lambda x:x['Nombre'])
                print(f"\n{GREEN}Resultados del ordenamiento por {YELLOW}NOMBRE{RESET} {GREEN}de mascota: {RESET}")
                for a in datosVet:
                    sleep(1)
                    print(f"⇢ Nombre: {a['Nombre']} ▸ Nacimiento: {a['Nacimiento']} ▸ Raza: {a['Raza']} ▸ Dueño: {a['Dueño']} ▸ DNI: {a['DNI']}")

            if opc_busq == 2:
                edMas = sorted(datosVet, key = lambda t: datetime.strptime(t['Nacimiento'], "%d/%m/%Y"))
                print(f"\n{GREEN}Resultados del ordenamiento por {YELLOW}EDAD{RESET} {GREEN}de mascota: {RESET}")
                for b in edMas:
                    sleep(1)
                    print(f"⇢  Nombre: {b['Nombre']} ▸ Nacimiento: {b['Nacimiento']} ▸ Raza: {b['Raza']} ▸ Dueño: {b['Dueño']} ▸ DNI: {b['DNI']}")

            if opc_busq == 3:
                datosVet.sort(key = lambda x:x['Raza'])
                print(f"\n{GREEN}Resultados del ordenamiento por {YELLOW}RAZA{RESET} {GREEN}de mascota: {RESET}")       
                for c in datosVet:
                    sleep(1)
                    print(f"⇢  Nombre: {c['Nombre']} ▸ Nacimiento: {c['Nacimiento']} ▸ Raza: {c['Raza']} ▸ Dueño: {c['Dueño']} ▸ DNI: {c['DNI']}")
            
            if opc_busq == 4:
                datosVet.sort(key = lambda x:x['Dueño'])
                print(f"\n{GREEN}Resultados del ordenamiento por {YELLOW}DUEÑO{RESET} {GREEN}de mascota: {RESET}")         
                for d in datosVet:
                    sleep(1)
                    print(f"⇢  Nombre: {d['Nombre']} ▸ Nacimiento: {d['Nacimiento']} ▸ Raza: {d['Raza']} ▸ Dueño: {d['Dueño']} ▸ DNI: {d['DNI']}")
            
            if opc_busq == 5:
                datosVet.sort(key = lambda x:x['DNI'])
                print(f"\n{GREEN}Resultados del ordenamiento por {YELLOW}DNI{RESET} {GREEN}de mascota: {RESET}")
                for e in datosVet:
                    sleep(1)
                    print(f"⇢  Nombre: {e['Nombre']} ▸ Nacimiento: {e['Nacimiento']} ▸ Raza: {e['Raza']} ▸ Dueño: {e['Dueño']} ▸ DNI: {e['DNI']}")

            if opc_busq == 6:
                sleep(2)
                return self.menu()
            
            if opc_busq == 7:
                print("¡Hasta luego, que tenga un buen día")
                sleep(1.5)
                self.salir()

        else:
            print("Elección incorrecta, vuelva a intentarlo."+RESET)
            sleep(2)

    # Crear una copia del registro veterinario
    def guardar(self):
        my_path = 'registro_2.csv'
        with open(my_path, 'w', encoding="utf-8",newline='') as newReg:
            writer = csv.DictWriter(newReg,fieldnames = self.fieldnames,delimiter=',')
            writer.writeheader()
            writer.writerows(self.listas)
        newReg.close()
        sleep(2.5)
        print(YELLOW+"\nSe ha creado un nuevo registro en el sistema con nombre registro_2.csv"+RESET)
        sleep(1)

    # Opción de salir del programa 
    def salir(self):
        exit()

vet = Veterinaria()
vet.menu()
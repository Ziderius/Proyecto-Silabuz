import pandas as pd
import csv
from time import sleep, time
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

    def menu(self):
        
    
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
    # agregar mas mascotas al archivo CSV

    def agregar_mascota(self):
        print("Necesitamos los siguientes datos de la mascota para su registro")
        nombre_mascota=input("Nombre mascota: ")
        nacimiento_mascota=input("Ingrese Dia, Mes y Año de nacimiento"
                        "(Separados por un guion slash / ): ")
        raza_mascota=input("raza Mascota: ")
        nombre_dueño=input("nombre del dueño: ")
        identificacion_Dni=int(input("identificacion: ")[0:8])
        list_add = [nombre_mascota,nacimiento_mascota,raza_mascota,nombre_dueño,identificacion_Dni]
        with open('registro.csv', 'a', encoding= "utf-8",newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow(list_add)  
            f_object.close()

    # buscar datos de el archivo CSV
    def buscar_mascota(self):
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
        
    # Submenú de ordenamiento por lo que el usuario requiera
    def busq(self):
        datosVet = self.listas
        opc_busq = 0
        while opc_busq != 7:
            time.sleep(1.5)
            print('''
            Submenú de ordenamiento del registro veterinario
            1 : Nombre de mascota
            2 : Edad
            3 : Raza
            4 : Dueño
            5 : DNI
            6 : Retornar al menú principal
            7 : Salir del programa''')
            time.sleep(1)
            opc_busq = int(input("\nIngrese su opción: "))
            time.sleep(2)

            if opc_busq == 1:
                datosVet.sort(key = lambda x:x['Nombre'])
                print("\nResultados del ordenamiento por Nombre de mascota: ")
                for a in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {a['Nombre']} ▸ Nacimiento: {a['Nacimiento']} ▸ Raza: {a['Raza']} ▸ Dueño: {a['Dueño']} ▸ DNI: {a['DNI']}")

            if opc_busq == 2:
                edMas = sorted(datosVet, key = lambda t: datetime.strptime(t['Nacimiento'], "%d/%m/%Y"))
                print("\nResultados del ordenamiento por Edad de mascota: ")
                for b in edMas:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {b['Nombre']} ▸ Nacimiento: {b['Nacimiento']} ▸ Raza: {b['Raza']} ▸ Dueño: {b['Dueño']} ▸ DNI: {b['DNI']}")

            if opc_busq == 3:
                datosVet.sort(key = lambda x:x['Raza'])
                print("\nResultados del ordenamiento por Raza de mascota: ")                
                for c in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {c['Nombre']} ▸ Nacimiento: {c['Nacimiento']} ▸ Raza: {c['Raza']} ▸ Dueño: {c['Dueño']} ▸ DNI: {c['DNI']}")
            
            if opc_busq == 4:
                datosVet.sort(key = lambda x:x['Dueño'])
                print("\nResultados del ordenamiento por Dueño de mascota: ")                
                for d in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {d['Nombre']} ▸ Nacimiento: {d['Nacimiento']} ▸ Raza: {d['Raza']} ▸ Dueño: {d['Dueño']} ▸ DNI: {d['DNI']}")
            
            if opc_busq == 5:
                datosVet.sort(key = lambda x:x['DNI'])
                print("\nResultados del ordenamiento por DNI del dueño: ")
                for e in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {e['Nombre']} ▸ Nacimiento: {e['Nacimiento']} ▸ Raza: {e['Raza']} ▸ Dueño: {e['Dueño']} ▸ DNI: {e['DNI']}")

            if opc_busq == 6:
                return self.menu()
            
            if opc_busq == 7:
                self.salir()

        else:
            print("Elección incorrecta, vuelva a intentarlo.")

    # Crear una copia del registro veterinario
    def guardar(self):
        my_path = 'registro_2.csv'
        with open(my_path, 'w', encoding="utf-8",newline='') as newReg:
            writer = csv.DictWriter(newReg,fieldnames = self.fieldnames,delimiter=',')
            writer.writeheader()
            writer.writerows(self.listas)
        newReg.close()
        time.sleep(2.5)
        print("\nSe ha creado un nuevo registro en el sistema con nombre registro_2.csv")
        time.sleep(1)

    # Opción de salir del programa 
    def salir(self):
        exit()

vet = Veterinaria()
vet.menu()

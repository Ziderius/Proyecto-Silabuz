import csv
import pandas as pd
from datetime import datetime, date
# módulo pandas: pip install pandas
import time
    
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
        while opc != 8:
            print('''
            ¡Bienvenido al Sistema de Registro Veterinario!
            5 : Ordenar mascotas por datos de registro.
            6 : Guardar los datos.
            7 : Salir. 
            ''')
            time.sleep(0)
            opc = int(input("Introduzca su opción: "))
            if opc == 5:
                self.busq()
            if opc == 6:
                self.cump()
            if opc == 7:
                self.salir()
            else:
                print("Elección no válida. Intente de nuevo.")
                time.sleep(2) 
                return self.menu()

    # Submenú de ordenamiento por lo que el usuario requiera
    def busq(self):
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
                datosVet = self.listas
                datosVet.sort(key = lambda x:x['Nombre'])
                print("\nResultados del ordenamiento por Nombre de mascota: ")
                for a in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {a['Nombre']} ▸ Nacimiento: {a['Nacimiento']} ▸ Raza: {a['Raza']} ▸ Dueño: {a['Dueño']} ▸ DNI: {a['DNI']}")

            if opc_busq == 2:
                datosVet = self.listas
                edMas = sorted(datosVet, key = lambda t: datetime.strptime(t['Nacimiento'], "%d/%m/%Y"))
                print("\nResultados del ordenamiento por Edad de mascota: ")
                for b in edMas:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {b['Nombre']} ▸ Nacimiento: {b['Nacimiento']} ▸ Raza: {b['Raza']} ▸ Dueño: {b['Dueño']} ▸ DNI: {b['DNI']}")

            if opc_busq == 3:
                datosVet = self.listas
                datosVet.sort(key = lambda x:x['Raza'])
                print("\nResultados del ordenamiento por Raza de mascota: ")                
                for c in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {c['Nombre']} ▸ Nacimiento: {c['Nacimiento']} ▸ Raza: {c['Raza']} ▸ Dueño: {c['Dueño']} ▸ DNI: {c['DNI']}")
            
            if opc_busq == 4:
                datosVet = self.listas
                datosVet.sort(key = lambda x:x['Dueño'])
                print("\nResultados del ordenamiento por Dueño de mascota: ")                
                for d in datosVet:
                    time.sleep(1)
                    print(f"\n⇢  Nombre: {d['Nombre']} ▸ Nacimiento: {d['Nacimiento']} ▸ Raza: {d['Raza']} ▸ Dueño: {d['Dueño']} ▸ DNI: {d['DNI']}")
            
            if opc_busq == 5:
                datosVet = self.listas
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

    # Opción de salir del programa 
    def salir(self):
        exit()

vet = Veterinaria()
vet.menu()
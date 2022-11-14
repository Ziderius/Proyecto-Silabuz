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

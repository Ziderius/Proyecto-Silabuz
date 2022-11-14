import pandas as pd
import csv
import random  # Importamos la librería random
import sys  #para finalizar el juego
import time  #para definir tiempo
from csv import writer
#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
time.sleep(1)  # Espera 1 segundos antes de continuar.
print(CYAN +"=== Bienvenido la veterinaria Kolitas=== ")
print("=== Elija una de las opciones diponibles ===\n" +RESET)
time.sleep(1)  # Espera 1 segundos antes de continuar.
def menu():
    print(YELLOW+ "presione 1 para  cargar datos de su mascota ")
    print("presione 2 para mostrar los datos de mascotas cargadas en el sistema")
    print("presione 3 para agregar mascota")
    print("presione 4 para buscar mascota")
    print("presione 5 para ordenar mascota")
    print("presione 6 para guardar mascotas \n" +RESET)
    opcion = int(input("Elija una opcion correcta: "))
    while opcion not in (1,2,3,4,5,6):
            opcion = input("la opcion no existe, elija una opcion correcta: ")
    if opcion == 3:
        agregar_mascota()
    if opcion == 4:
        buscar_mascota()

def agregar_mascota():
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

def buscar_mascota():
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
menu()
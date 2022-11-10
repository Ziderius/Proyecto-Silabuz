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
import random  # Importamos la librería random
import sys  #para finalizar el juego
import time  #para definir tiempo
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
    while  opcion not in (1,2,3,4,5,6):
        opcion = input("la opcion no existe, elija una opcion correcta: ")
    if opcion == 1:
        print("te llamas pedro")
        #carga()
menu()
'''
    if opcion==1:
        carga()

    if opcion==2:
        mostrar()
    if opcion==3:
        agregar()
    if opcion==4:
        buscar()
    if ordenar==5:
        cargar()
    elif opcion==6:
        guardar(datos)
def carga():
    datos={}
    continua="s"
    while continua=="s":
        legajos=int(input("ingrese numero de legajo"))
        
        nombre=input("ingrese nombre del empleado")
        profesion=input("ingrese puesto /area/profesion")
        sueldo=int(input("ingrese sueldo del empleado"))
        datos[legajos]=[nombre,profesion,sueldo]
        continua=input("desea agregar otro empleado?")
        if continua!="s":
            menu()      
    return(datos)
   

def mostrar():
    
def agregar():
    
def buscar():
    
def cargar():
    
def guardar():


def modicar(datos):
    legajo=int(input("ingrese numero de legajo a seleccionar"))
    if legajo in datos:
        sueldo=int(input("ingrese el nuevo sueldo"))
        datos[2]=sueldo
'''
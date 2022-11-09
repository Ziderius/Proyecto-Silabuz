def menu():
    print("presione 1 para  cargar datos de su mascota")
    print("presione 2 para mostrar los datos de mascotas cargadas en el sistema")
    print("presione 3 para agregar mascota")
    print("presione 4 para buscar mascota")
    print("presione 5 para ordenar mascota")
    print("presione 6 para guardar mascotas ")
    opcion=int(input("ingrese una opcion correcta"))
    if opcion==1:
        carga()
    elif opcion==2:
        modicar(datos)
        
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
   


def modicar(datos):
    legajo=int(input("ingrese numero de legajo a seleccionar"))
    if legajo in datos:
        sueldo=int(input("ingrese el nuevo sueldo"))
        datos[2]=sueldo
#importar modulos
import validaciones
import procesamiento


#Solicitar cantidad para determinar valor de listas
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos [Entre 1 y 30]: "))

while cantidad_alumnos <1  or cantidad_alumnos >30: #validacion
    cantidad_alumnos = int(input("Valor inválido. Ingrese otro valor (Entre 1 y 30): "))
        

#Inicializacion de las listas paralelas
nombres = [""] * cantidad_alumnos #str
parcial_1 = [0] * cantidad_alumnos #int
parcial_2 = [0] * cantidad_alumnos #int
promedio = [0] * cantidad_alumnos #int

        

#Carga de datos 

for i in range(cantidad_alumnos):
    nombres[i] = input("Ingrese el nombre del alumno/a: ")
    
    while not validaciones.validar_nombre(nombres[i]): #Validar que sea con más de 5 caracteres. No números, no espacio.
        print("Nombre inválido, debe tener al menos 5 caracteres.")
        nombres[i] = input("Ingrese el nombre del alumno: ")
    
    
    parcial_1[i] = int(input("Ingrese la nota del parcial 1 (1 a 10): ")) #Ingresa nota  parcial 1(int)
    
    while not validaciones.validar_nota(parcial_1[i]): #Llamar a la funcion para validar que la nota esté dentro del 1 al 10
        parcial_1[i] = int(input("Número inválido. Ingrese un número del 1 al 10 para la primer nota: "))
    
    
    parcial_2[i] = int(input("Ingrese la nota del parcial 2 (1 a 10): ")) #Ingresa nota parcial 2(int)
    
    while not validaciones.validar_nota(parcial_2[i]): #Llamar a la funcion para validar que la nota esté dentro del 1 al 10
            parcial_2[i] = int(input("Número inválido. Ingrese un número del 1 al 10 para la segunda nota: "))

    #Calcular promedio de cada alumno
    promedio[i] = procesamiento.calcular_promedio(parcial_1[i], parcial_2[i])


#Mostrar datos    
procesamiento.mostrar_datos(nombres, parcial_1, parcial_2, promedio)



# Mostrar promedio general (4 estadisticas)
promedio_general = procesamiento.calcular_promedio_general(promedio)
print(f"El promedio general del curso es: {promedio_general}")

#Mejor promedio (4 estadisticas)
"""
mejor_promedio, nombre_maximo = procesamiento.calcular_maximo(promedio, nombres)
print(f"Mejor promedio {maximo}, Alumno/a: {nombres}")
pass
peor_promedio, nombre_minimo = procesamiento.calcular_minimo(promedio, nombres)
print(f"Peor promedio {minimo}, Alumno/a: {nombres}")   
pass 
"""

#Cantidad de alumnos por condicion (4 estadisticas)
promociona, aprueba, desaprueba = procesamiento.calcular_condicion(promedio)

print(f"Cantidad de alumnos que promocionan: {promociona}")
print(f"Cantidad de alumnos que aprueban: {aprueba}")
print(f"Cantidad de alumnos que desaprueban: {desaprueba}")



# Ranking 5 - Curso ordenado por promedio  - del mejor al peor

promedio, nombres = procesamiento.ordenar_burbuja(promedio, nombres)

for i in range(len(promedio)):
    print(f"Alumno/a: {nombres[i]} - Promedio: {promedio[i]}")


#6. Juegos con nombre
#Contar vocales
nombre_ingresado = input("Ingrese un nombre para contar sus vocales: ")
total_vocales = procesamiento.contar_vocales(nombre_ingresado)

print(f"El nombre del alumno/a tiene {total_vocales} vocales. ")


#Invertir nombre 
nombre_ingresado = input("Ingrese el nombre que desea invertir: ")
nombre_invertido = procesamiento.invertir_nombre(nombre_ingresado)

print(f"Nombre invertido: {nombre_invertido}")



#7. Busqueda 
nombre_buscado = input("Ingrese el nombre del alumno que desea buscar: ")

procesamiento.buscar_alumno(nombre_buscado, nombres, parcial_1, parcial_2, promedio)



#recordar  el menu va dentro de una funcion
#importar modulos
import validaciones
import procesamiento

def iniciar_menu():
    nombres = []
    parcial_1 = []
    parcial_2 = []
    promedio = []

    alumnos_cargados = False
    opcion = ""
    
    while opcion != "0":
    
        opcion = input(
                "¡Hola Laura, bienvenida a tu nuevo programa de notas!\n"
                "========= NOTA FÁCIL =========\n"
                "1. Cargar alumnos\n"
                "2. Mostrar listado\n"
                "3. Mostrar estadísticas\n"
                "4. Ver ranking \n"
                "5. Buscar alumno\n"
                "6. Juegos con un nombre\n"
                "0. Salir\n"
                "Selecciona una opción para continuar: "
            )
        
        match opcion:
            case "1":
                #Carga de datos 
                #Solicitar cantidad para determinar valor de listas
                cantidad_alumnos = validaciones.validar_cantidad()
                    
                #Inicializacion de las listas paralelas
                nombres = [""] * cantidad_alumnos #str
                parcial_1 = [0] * cantidad_alumnos #int
                parcial_2 = [0] * cantidad_alumnos #int
                promedio = [0] * cantidad_alumnos #int
        
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
                    
                print("Alumnos cargados con éxito.")
                alumnos_cargados = True
                    
                    
            case "2":
                #Mostrar datos   
                if alumnos_cargados == True:
                    procesamiento.mostrar_datos(nombres, parcial_1, parcial_2, promedio)
                else:
                    print("Error. Recuerde, antes debe cargar alumnos.")
            
            
            case "3": #Estadísticas
                
                if alumnos_cargados == True:
                    # Mostrar promedio general
                    promedio_general = procesamiento.calcular_promedio_general(promedio)
                    print(f"El promedio general del curso es: {promedio_general}")
                    
                    
                    #Mejor promedio
                    mejor_promedio, nombre_maximo = procesamiento.calcular_maximo(promedio, nombres)
                    print(f"Mejor promedio: {mejor_promedio}, Alumno/a: {nombre_maximo}")
                    
                    peor_promedio, nombre_minimo = procesamiento.calcular_minimo(promedio, nombres)
                    print(f"Peor promedio: {peor_promedio}, Alumno/a: {nombre_minimo}")
                    
                    
                    #Cantidad de alumnos por condicion 
                    promociona, aprueba, desaprueba = procesamiento.calcular_condicion(promedio)
                    
                    print(f"Cantidad de alumnos que promocionan: {promociona}")
                    print(f"Cantidad de alumnos que aprueban: {aprueba}")
                    print(f"Cantidad de alumnos que desaprueban: {desaprueba}")
                
                else:     
                    print("Error. Recuerde, antes debe cargar alumnos.")

        
            case "4": #Ranking
                if alumnos_cargados == True:
                    promedio, nombres = procesamiento.ordenar_burbuja(promedio, nombres)

                    for i in range(len(promedio)):
                        print(f"Alumno/a: {nombres[i]} - Promedio: {promedio[i]}")
                else:     
                    print("Error. Recuerde, antes debe cargar alumnos.")
                    
                        
            case "5": #Buscar alumno
                if alumnos_cargados == True:
                    nombre_buscado = input("Ingrese el nombre del alumno que desea buscar: ")
                    procesamiento.buscar_alumno(nombre_buscado, nombres, parcial_1, parcial_2, promedio)

                else:     
                    print("Error. Recuerde, antes debe cargar alumnos.")
        
        
            case "6": #Juegos con un nombre
                #Contar vocales
                nombre_ingresado = input("Ingrese un nombre para contar sus vocales: ")
                total_vocales = procesamiento.contar_vocales(nombre_ingresado)

                print(f"El nombre del alumno/a tiene {total_vocales} vocales. ")

                #Invertir nombre 
                nombre_ingresado = input("Ingrese el nombre que desea invertir: ")
                nombre_invertido = procesamiento.invertir_nombre(nombre_ingresado)

                print(f"Nombre invertido: {nombre_invertido}")
                
                
            case "0":
                print("Ha seleccionado la opción SALIR. Hasta pronto.")

            case _:
                print("Opción no válida. Ingrese una opción de 1 al 6 (o 0 para SALIR): ")


iniciar_menu()
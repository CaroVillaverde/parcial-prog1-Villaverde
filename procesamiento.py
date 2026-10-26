
#Mostrar datos 
def mostrar_datos(nombres, parcial_1, parcial_2, promedio): 
    """Muestra el nombre, las notas y el promedio de cada alumno"""
    
    for i in range(len(nombres)):
        print(f"Alumno/a: {nombres[i]}\n"
            f"Nota parcial 1: {parcial_1[i]}\n"
            f"Nota parcial 2: {parcial_2[i]}\n"
            f"Su promedio es: {promedio[i]}\n")
    
    
#Calcular promedio   
def calcular_promedio(parcial_1, parcial_2):
    """Toma los valores de la nota 1 y la nota 2, los suma y divide el resultado por 2"""
    return (parcial_1 + parcial_2 ) / 2


#Calcular promedio general
def calcular_promedio_general(promedio):
    """ suma el promedio de cada alumno y lo divide por la cantidad de promedios que haya.
        para dar un promedio general"""
        
    acumulador = 0
    
    for i in range(len(promedio)):
        acumulador += promedio[i]
        
    promedio_general = acumulador / len(promedio)
    
    return promedio_general



def calcular_maximo(promedio, nombres):
    """ calcula el mejor promedio """
    
    maximo = promedio[0]
    nombre_maximo = 0
    
    for i in range (1, len(promedio)):
        if promedio[i] > maximo:
            maximo = promedio[i]
            nombre_maximo = i

    return maximo, nombres[nombre_maximo]



def calcular_minimo(promedio, nombres):
    """ calcula el peor promedio """
    minimo = promedio[0]
    nombre_minimo = 0
    
    for i in range (1, len(promedio)):
        if promedio[i] < minimo:
            minimo = promedio[i]
            nombre_minimo = i
    
    return minimo, nombres[nombre_minimo]


#Calcular condicion
def calcular_condicion(promedio):
    """Calcula cantidad de alumnos por condicion, entre promociona, aprueba o desaprueba"""
    promociona = 0
    aprueba = 0
    desaprueba = 0 
    
    for i in range (len(promedio)):
        if promedio[i] >= 6:
            promociona += 1 
        elif promedio[i] >= 4 and promedio[i] < 6:
            aprueba += 1   
        else: 
            desaprueba += 1 
            
    return promociona, aprueba, desaprueba


def ordenar_burbuja(promedio, nombres):
    """  - Curso ordenado por promedio -del mejor al peor- Ordenamiento burbuja """
    
    cantidad = len(promedio)
        
    for i in range(cantidad):
        for j in range(cantidad - 1):
            if promedio[j] < promedio[j + 1]:
                
                variable_auxiliar = promedio[j]
                promedio[j] = promedio[j + 1]
                promedio[j + 1] = variable_auxiliar
                
                variable_auxiliar = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = variable_auxiliar 
                
    return promedio, nombres


def invertir_nombre(nombre_ingresado):
    """ Invierte el nombre que se ingresa """
    
    invertido = ""
    
    for i in range(len(nombre_ingresado)):
        invertido = nombre_ingresado[i] + invertido
        
    return invertido


def contar_vocales(nombre_ingresado):
    """ Cuenta las vocales del nombre ingresado"""
    vocales = "aeiou"
    contador = 0
    
    for i in range(len(nombre_ingresado)):
        
        for j in range(len(vocales)): 
            if nombre_ingresado[i] == vocales[j]:
                contador += 1 
    
    return contador       
            

#Buscar alumno
def buscar_alumno(nombre_buscado, nombres, parcial_1, parcial_2, promedio):
    """ Compara el nombre ingresado con la lista de nombres, si coincide muestra los datos del alumno"""
    coincide = False

    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            print(f"Alumno: {nombres[i]}")
            print(f"Nota parcial 1: {parcial_1[i]}")
            print(f"Nota parcial 2: {parcial_2[i]}")
            print(f"Promedio: {promedio[i]}")
        
            coincide = True
            break
    
    if coincide == False: 
            print("El alumno no se encuentra en la lista.")        

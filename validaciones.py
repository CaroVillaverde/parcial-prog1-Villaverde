
# Validar cantidad
def validar_cantidad():
    valido = False
    
    while not valido:
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos [Entre 1 y 30]: "))
        if 1 <= cantidad_alumnos <= 30:
            valido = True
        else: 
            print("Error, ingrese un número entre 1 y 30:") 
    
    return cantidad_alumnos 


# validar nombre
def validar_nombre(nombres):
    """Valida que el nombre tenga al menos 5 caracteres y no contenga números o espacios."""
    if len(nombres) < 5:
        return False 
    
    for i in range(len(nombres)):
        caracter = nombres[i] #Cada posicion del nombre que de el usuario
        
        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z"
        espacio = caracter == " "
        
        if not (minuscula or  mayuscula or espacio):
            return False 
    return True  


#Validar nota
def validar_nota(nota):
    """ Valida que el número ingresado esté entre el 1 y el 10"""
    if  nota < 1  or nota > 10:
        return False 
    return True
    



    
    


# Replace the "ANSWER HERE" for your answer

def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    for i in range(len(lst)):
        if lst[i] == "": # Si encontré un lugar vacío
            lst[i] = value # Lo ocupo con el nuevo valor
            return i # Devuelvo la posición donde lo puse y CORTO la función
            
    return -1 # Si terminó el for y no había ningún ""

def remove(value, lst):
    """
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """
   
    contador_borrados = 0
    
    for i in range(len(lst)):
        if lst[i] == value:
            lst[i] = "" # Lo borramos dejando el string vacío
            contador_borrados = contador_borrados + 1
            
    return contador_borrados # Devolvemos el total de veces que lo borramos

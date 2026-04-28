# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    resultado = []
    i = 0  # Este es tu contador manual
    
    for palabra in lst:
        if palabra != "":  # Solo si NO es un string vacío
            # Armamos el string con el formato "indice. valor"
            formato = f"{i}. {palabra}"
            resultado.append(formato)
            i = i + 1  # SOLO sumamos si agregamos una palabra
            
    return resultado

def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    resultado = []
    i = 0
    
    for palabra in lst:
        if palabra != "":
            # Invertimos la palabra con slicing
            palabra_al_reves = palabra[::-1]
            resultado.append(f"{i}. {palabra_al_reves}")
            i = i + 1
            
    return resultado
